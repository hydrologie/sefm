import numpy as np
from rasterio import features
from affine import Affine
import pandas as pd
import xarray as xr
import os
import geopandas as gpd
import s3fs


def transform_from_latlon(lat, lon):
    """ input 1D array of lat / lon and output an Affine transformation
    """
    lat = np.asarray(lat)
    lon = np.asarray(lon)
    trans = Affine.translation(lon[0], lat[0])
    scale = Affine.scale(lon[1] - lon[0], lat[1] - lat[0])
    return trans * scale


def rasterize(shapes, coords, latitude='latitude', longitude='longitude',
              fill=np.nan, **kwargs):
    """
    """
    transform = transform_from_latlon(coords[latitude], coords[longitude])
    out_shape = (len(coords[latitude]), len(coords[longitude]))
    raster = features.rasterize(shapes, out_shape=out_shape,
                                fill=fill, transform=transform,
                                dtype=float, **kwargs)
    spatial_coords = {latitude: coords[latitude], longitude: coords[longitude]}
    return xr.DataArray(raster, coords=spatial_coords, dims=(latitude, longitude))


def files_to_gdf(url,
                 epsg=4326,
                 client_kwargs=None):
    lst_shp = []

    # if file
    if url.startswith(('s3://')):
        s3 = s3fs.S3FileSystem(client_kwargs=client_kwargs,
                               anon=True)  # public read
        if url.endswith(('.shp', '.json', 'geojson')):
            lst_shp = [url]
            gdf = pd.concat([gpd.GeoDataFrame.from_file(s3.open(file), encoding='latin-1')
                             for file in lst_shp])
        else:
            try:
                lst_shp = ['s3://' + f for f in s3.find(url)
                           if f.endswith(('.shp', '.json', 'geojson'))]
                gdf = pd.concat([gpd.GeoDataFrame.from_file(s3.open(file), encoding='latin-1')
                                 for file in lst_shp])
            except:
                raise NameError('folder not found in the cloud or file extension not supported')

    # if directory
    else:
        if url.endswith(('.shp', '.json', 'geojson')):
            lst_shp = [url]
            gdf = pd.concat([gpd.GeoDataFrame.from_file(file, encoding='latin-1')
                             for file in lst_shp])
        else:
            for dirpath, dirnames, filenames in os.walk(url):
                for filename in [f for f in filenames
                                 if f.endswith(('.shp', '.json', 'geojson'))]:
                    lst_shp.append(os.path.join(dirpath, filename))
            gdf = pd.concat([gpd.GeoDataFrame.from_file(file, encoding='latin-1')
                             for file in lst_shp])
    # create geopandas from files

    gdf = gdf.reset_index().drop(columns=['index'])

    # Set initial epsg
    gdf.crs = {'init': 'epsg:{}'.format(epsg)}
    return gdf.to_crs(epsg=4326)


def clip_polygon_to_dataframe(dataset,
                              geodataframe,
                              geodf_index_column,
                              variable,
                              aggregation='mean',
                              resample_time=None,
                              from_tz='UTC',
                              to_tz='UTC',
                              latlng_names=['latitude', 'longitude']
                              ):
    list_df = []

    if not geodataframe.empty:
        if geodf_index_column in geodataframe.columns:
            # make sure all values are strings
            geodataframe.loc[:, geodf_index_column] = geodataframe[geodf_index_column].astype(str)

            # Iterate on each polygon
            for idx, row in geodataframe.iterrows():

                use_centroid = False

                name = row[geodf_index_column]
                print(name)
                # Rasterize polygon to DataArray format
                mask = rasterize([row.geometry], dataset.coords,
                                 latitude=latlng_names[0],
                                 longitude=latlng_names[1])

                # Get all latitude/longitude values of polygon
                sel_mask = mask.where(mask == 1).values
                lat = mask.latitude.values
                lon = mask.longitude.values
                id_lon = lon[np.where(~np.all(np.isnan(sel_mask), axis=0))]
                id_lat = lat[np.where(~np.all(np.isnan(sel_mask), axis=1))]
                # If polygon is too small, use centroid instead
                if not any(id_lon):
                    use_centroid = True
                    id_lon = np.append(id_lon,
                                       min(lon, key=lambda x: abs(row.geometry.centroid.coords.xy[0][0] - x)))
                if not any(id_lat):
                    use_centroid = True
                    id_lat = np.append(id_lat,
                                       min(lat, key=lambda x: abs(row.geometry.centroid.coords.xy[1][0] - x)))

                # Clip DataArray to keep only the polygon mask
                if use_centroid:
                    ds_clip = dataset.sel(latitude=slice(id_lat[0], id_lat[-1]),
                                     longitude=slice(id_lon[0], id_lon[-1]))[variable]
                else:
                    ds_clip = dataset.sel(latitude=slice(id_lat[0], id_lat[-1]),
                                     longitude=slice(id_lon[0], id_lon[-1]))[variable].where(mask == 1)

                ds_agg = ds_clip.mean(['latitude', 'longitude'])
                df_idx = ds_agg.rename(name).to_dataframe()
                df_idx.index = df_idx.index.tz_localize(from_tz).tz_convert(to_tz)

                if resample_time is not None:
                    if aggregation is 'mean':
                        df_out = df_idx.resample(resample_time).mean()
                    elif aggregation is 'sum':
                        df_out = df_idx.resample(resample_time).sum()
                    elif aggregation is 'max':
                        df_out = df_idx.resample(resample_time).max()
                    elif aggregation is 'min':
                        df_out = df_idx.resample(resample_time).min()
                    else:
                        raise NameError('aggregation or resampling method not valid')

                list_df.append(df_out)
            return pd.concat(list_df, axis=1)