from urllib.request import urlopen
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import json
import pandas as pd

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

app = DjangoDash('UsaGraph')

app.layout = html.Div([
        html.Label(title='Gráfico'),
        dcc.Graph(id='usa_fig', animate=True)
])

@app.callback(
    Output('usa_fig', 'figure'),
)

def map():

    trace = []

    fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.fips, z=df.unemp,
                                        colorscale="Viridis", zmin=0, zmax=12,
                                        marker_opacity=0.5, marker_line_width=0))
    fig.update_layout(mapbox_style="carto-positron",
                      mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    trace.append(fig)

    layout = go.layout(title='USA')

    return {'data': [trace], 'layout':layout}
