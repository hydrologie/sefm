import dask.dataframe as dd
import plotly.graph_objects as go
import plotly.express as px
import geopandas as gpd
import json
import hvplot
import holoviews as hv
from geoviews import opts
import os
import pandas as pd
import numpy as np
import geoviews.feature as gf


class Stations:
    def __init__(self, metadata_bucket, storage_options=None):
        """

        Parameters
        ----------
        metadata_bucket
        storage_options
        """

        # TODO : Handle Exceptions

        self.metadata_bucket = metadata_bucket
        self.storage_options = storage_options
        self.metadata = None

    def read_metadata(self,
                      station_names=None,
                      latlngbox=None):
        """

        Parameters
        ----------
        station_names
        latlngbox

        Returns
        -------

        """

        ddf = dd.read_csv(urlpath=self.metadata_bucket,
                          storage_options=self.storage_options)

        if station_names is not None:
            # convert to array if single string was passed
            station_names = [station_names] if isinstance(station_names, str) else station_names

            ddf = ddf[ddf.id.isin(station_names)].compute()

        elif latlngbox is not None and station_names is None:
            ddf = ddf[ddf['longitude'].between(latlngbox[0], latlngbox[1]) &
                      ddf['latitude'].between(latlngbox[2], latlngbox[3])].compute()
        else:
            ddf = ddf.compute()

        self.metadata = ddf

        return ddf

    def read_csv(self,
                 bucket,
                 element=None,
                 storage_options=None):
        """

        Parameters
        ----------
        bucket
        element
        storage_options

        Returns
        -------

        """

        if storage_options is None:
            storage_options = self.storage_options

        element = [element] if isinstance(element, str) else element

        df = dd.read_csv(bucket, storage_options=storage_options)
        return df.loc[df.loc(self.metadata.id) & df.element.isin(element)].compute()

    def read_parquet(self,
                     bucket,
                     element=None,
                     storage_options=None):
        """

        Parameters
        ----------
        bucket
        element
        storage_options

        Returns
        -------

        """

        if storage_options is None:
            storage_options = self.storage_options

        element = [element] if isinstance(element, str) else element

        ddf = dd.read_parquet(bucket,
                              engine='pyarrow',
                              storage_options=storage_options)

        ddf = ddf.loc[ddf.index.isin(self.metadata.id)]

        if element is not None:
            ddf = ddf.loc[ddf.element.isin(element)]

        return ddf.compute().reset_index()

    def plot_stations(self):
        """

        Returns
        -------

        """
        hv.extension('bokeh')

        opts.defaults(
                opts.Overlay(active_tools=['wheel_zoom', 'pan']))

        return (gf.ocean*gf.land*gf.ocean* gf.borders) *\
            self.metadata.hvplot.points('longitude', 'latitude',
                                        hover_cols=['id','name'],
                                        grid=True, width=800, height=500,
                                        project=True,  alpha=0.8,
                                        xlim=(-81, -74), ylim=(44, 49.2), tiles='EsriUSATopo')


# def get_metadata_stations(bucket,
#                           latlngbox,
#                           storage_options):
#     df = dd.read_csv(bucket, storage_options=storage_options)
#     return df[df['longitude'].between(latlngbox[0], latlngbox[1]) & df['latitude'].between(latlngbox[2],
#                                                                                            latlngbox[3])].compute()
#
#
# def get_metadata_stations_all(bucket,
#                               storage_options):
#     return dd.read_csv(bucket, storage_options=storage_options)
#
#
# def get_data_stations(bucket,
#                       metadata_stations,
#                       element,
#                       storage_options):
#     df = dd.read_csv(bucket, storage_options=storage_options)
#     return df.loc[df.id.isin(metadata_stations.id) & df.element.isin(element)].compute()
#
#
# def crop_zone(df, latlngbox):
#     gdf = gpd.GeoDataFrame(
#         df, geometry=gpd.points_from_xy(x=df['Longitude (Decimal Degrees)'], y=df['Latitude (Decimal Degrees)'])
#     )
#     return gdf[gdf['Longitude (Decimal Degrees)'].between(latlngbox[0], latlngbox[1])
#            & gdf['Latitude (Decimal Degrees)'].between(latlngbox[2], latlngbox[3])]
#
#
# def visualisation_stations(gdf, df_stations, latlngbox):
#     chro = px.choropleth(gdf.reset_index().drop(columns=['geometry']),
#                         geojson=json.loads(gdf.to_json()), locations='index',
#                         hover_name="NOM",
#                         title='Bassin Outaouais',
#                         )
#
#     sc = go.Scattergeo(
#             lon = df_stations['longitude'],
#             lat = df_stations['latitude'],
#             text = df_stations['name'],
#             mode = 'markers',
#             marker_color ='red',
#             name = 'Stations météo'
#             )
#
#     fig = go.Figure(data=[sc, chro.data[0]])
#
#
#     fig.update_layout(
#             title = 'Station météorologiques contenant des données de précipitations (PRCP)',
#             geo = dict(
#                 showland = True,
#                 showsubunits = True,
#                 showcountries = True,
#                 resolution = 50,
#                 showlakes = True,
#                 lonaxis = dict(
#                     showgrid = True,
#                     gridwidth = 0.5,
#                     range= [ latlngbox[0] - 1, latlngbox[1] + 1],
#                     dtick = 5
#                 ),
#                 lataxis = dict (
#                     showgrid = True,
#                     gridwidth = 0.5,
#                     range= [ latlngbox[2] - 1, latlngbox[3] + 1],
#                     dtick = 5
#                 )
#             )
#     )
#     return fig.show()