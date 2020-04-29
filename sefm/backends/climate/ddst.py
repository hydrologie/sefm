import dask.dataframe as dd
import plotly.graph_objects as go
import plotly.express as px
import geopandas as gpd
import json


def get_metadata_stations(bucket,
                          latlngbox,
                          storage_options):
    df = dd.read_csv(bucket, storage_options=storage_options)
    return df[df['longitude'].between(latlngbox[0], latlngbox[1]) & df['latitude'].between(latlngbox[2],
                                                                                           latlngbox[3])].compute()


def get_metadata_stations_all(bucket,
                              storage_options):
    return dd.read_csv(bucket, storage_options=storage_options)


def get_data_stations(bucket,
                      metadata_stations,
                      element,
                      storage_options):
    df = dd.read_csv(bucket, storage_options=storage_options)
    return df.loc[df.id.isin(metadata_stations.id) & df.element.isin(element)].compute()


def crop_zone(df, latlngbox):
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(x=df['Longitude (Decimal Degrees)'], y=df['Latitude (Decimal Degrees)'])
    )
    return gdf[gdf['Longitude (Decimal Degrees)'].between(latlngbox[0], latlngbox[1])
           & gdf['Latitude (Decimal Degrees)'].between(latlngbox[2], latlngbox[3])]


def visualisation_stations(gdf, df_stations, latlngbox):
    chro = px.choropleth(gdf.reset_index().drop(columns=['geometry']),
                        geojson=json.loads(gdf.to_json()), locations='index',
                        hover_name="NOM",
                        title='Bassin Outaouais',
                        )

    sc = go.Scattergeo(
            lon = df_stations['longitude'],
            lat = df_stations['latitude'],
            text = df_stations['name'],
            mode = 'markers',
            marker_color ='red',
            name = 'Stations météo'
            )

    fig = go.Figure(data=[sc, chro.data[0]])


    fig.update_layout(
            title = 'Station météorologiques contenant des données de précipitations (PRCP)',
            geo = dict(
                showland = True,
                showsubunits = True,
                showcountries = True,
                resolution = 50,
                showlakes = True,
                lonaxis = dict(
                    showgrid = True,
                    gridwidth = 0.5,
                    range= [ latlngbox[0] - 1, latlngbox[1] + 1],
                    dtick = 5
                ),
                lataxis = dict (
                    showgrid = True,
                    gridwidth = 0.5,
                    range= [ latlngbox[2] - 1, latlngbox[3] + 1],
                    dtick = 5
                )
            )
    )
    return fig.show()