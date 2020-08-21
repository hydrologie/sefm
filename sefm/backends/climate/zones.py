import os
import pandas as pd
import geopandas as gpd
import hvplot
import hvplot.pandas
import holoviews as hv
from geoviews import opts
import geoviews as gv
import geoviews.feature as gf
import s3fs


class Zones:
    """

    """

    def __init__(self,
                 zones,
                 bucket,
                 client_kwargs=None):
        """

        Parameters
        ----------
        metadata_bucket
        storage_options
        """

        # TODO : Handle Exceptions

        self.bucket = bucket
        self.client_kwargs = client_kwargs
        self.zones = zones
        self.data = self.read_zones()

    def read_zones(self):
        """

        Parameters
        ----------
        station_names
        latlngbox

        Returns
        -------

        """
        zones = self.zones

        s3 = s3fs.S3FileSystem(client_kwargs=self.client_kwargs,
                               anon=True)  # public read

        for key, value in zones.items():
            zones[key]['gdf'] = pd.concat([gpd.GeoDataFrame.from_file(s3.open(os.path.join(self.bucket,
                                                                                           file)), encoding='latin-1')
                                           for file in zones[key]['filenames']])
        return zones

    def interactive_map(self):

        maps = []

        for key, value in self.data.items():
            print(key)

            if key != 'background':
                line_plot = None
                for unique_type in value['gdf'].geometry.type.unique():
                    print(unique_type)
                    gdf = value['gdf'].loc[value['gdf'].geometry.type.isin([unique_type])]
                    print(gdf.columns)
                    if unique_type == 'MultiPolygon' or unique_type == 'Polygon':
                        zone_plot = gdf.hvplot(hover_cols=['id'], colorbar=False,
                                               legend=False, label='id',
                                               grid=True, width=600, height=450,
                                               project=True, alpha=0.6, tiles='EsriUSATopo')
                        print(zone_plot.values()[0])
                        data = list(zip(zone_plot.Polygons.values()[0].data.geometry.centroid.x,
                                        zone_plot.Polygons.values()[0].data.geometry.centroid.y))

                        labels = hv.Labels({('x', 'y'): data,
                                            'text': [i for i in gdf['id']]},
                                           ['x', 'y'], 'text') \
                            .opts(opts.Labels(text_font_size='16pt'))

                    elif unique_type == 'MultiLineString':
                        line_plot = gdf.hvplot(project=True)
                if line_plot is not None:

                    interactive_map = (gf.ocean * gf.land * gf.ocean * gf.borders) * \
                                      zone_plot * \
                                      labels * \
                                      self.data['background']['gdf'].hvplot(project=True, alpha=0.1) * \
                                      line_plot
                else:
                    interactive_map = (gf.ocean * gf.land * gf.ocean * gf.borders) * \
                                      zone_plot * \
                                      labels * \
                                      self.data['background']['gdf'].hvplot(project=True, alpha=0.1)

                maps.append(interactive_map)

        return hv.Layout(maps).cols(2).opts(shared_axes=False)