import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd


from django_plotly_dash import DjangoDash
from plotly import graph_objs as go
from plotly.graph_objs import *
from dash.dependencies import Input, Output

path = "https://raw.githubusercontent.com/johnatasr/Data/master/NYC_Wi-Fi_Hotspot_Locations.csv"
css = 'https://codepen.io/amyoshino/pen/jzXypZ.css'

app = DjangoDash('wifinyc', add_bootstrap_links=css)
# app = dash.Dash()
# server = app.server
app.title = 'Pontos de Wifi de Nova York'

mapbox_access_token = 'pk.eyJ1Ijoiam9obmF0YXNyIiwiYSI6ImNrMmY3d2poYzBoYnAzY28wYmg1MjkwMnMifQ.BGIBMbj5heJP-sRpzvL7rQ'
map_data = pd.read_csv(path)

# Selecione as colunas
map_data = map_data[["Borough", "Type", "Provider", "Name", "Location", "Latitude", "Longitude"]].drop_duplicates()

# Boostrap CSS.
app.css.append_css({'external_url': css})

#  Layouts
layout_table = dict(
    autosize=True,
    height=500,
    font=dict(color="#191A1A"),
    titlefont=dict(color="#191A1A", size='14'),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor='#fffcfc',
    paper_bgcolor='#fffcfc',
    legend=dict(font=dict(size=10), orientation='h'),
)
layout_table['font-size'] = '12'
layout_table['margin-top'] = '20'

layout_map = dict(
    autosize=True,
    height=500,
    font=dict(color="#191A1A"),
    titlefont=dict(color="#191A1A", size='14'),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor='#fffcfc',
    paper_bgcolor='#fffcfc',
    legend=dict(font=dict(size=10), orientation='h'),
    title='WiFi Hotspots in NYC',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="light",
        center=dict(
            lon=-73.91251,
            lat=40.7342
        ),
        zoom=10,
    )
)

# functions
def gen_map(map_data):

    return {
        "data": [{
                "type": "scattermapbox",
                "lat": list(map_data['Latitude']),
                "lon": list(map_data['Longitude']),
                "hoverinfo": "text",
                "hovertext": [["Nome: {} <br>Tipo: {} <br>Provisor: {}".format(i, j, k)]
                                for i, j, k in zip(map_data['Name'], map_data['Type'], map_data['Provider'])],
                "mode": "markers",
                "name": list(map_data['Name']),
                "marker": {
                    "size": 6,
                    "opacity": 0.7
                }
        }],
        "layout": layout_map
    }

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='Mapas e Tabelas',
                        className='nine columns'),
                html.Img(
                    src="",
                    className='three columns',
                    style={
                        'height': '16%',
                        'width': '16%',
                        'float': 'right',
                        'position': 'relative',
                        'padding-top': 12,
                        'padding-right': 0
                    },
                ),
                html.Div(children='Culuna Teste',
                        className='nine columns'
                )
            ], className="row"
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.P('Escolhas os Bairros:'),
                        dcc.Checklist(
                                id='boroughs',
                                options=[
                                    {'label': 'Manhattan', 'value': 'MN'},
                                    {'label': 'Bronx', 'value': 'BX'},
                                    {'label': 'Queens', 'value': 'QU'},
                                    {'label': 'Brooklyn', 'value': 'BK'},
                                    {'label': 'Staten Island', 'value': 'SI'}
                                ],
                                value=['MN', 'BX', "QU",  'BK', 'SI'],
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
                html.Div(
                    [
                        html.P('Type:'),
                        dcc.Dropdown(
                            id='type',
                            options=[{'label': str(item),
                                                  'value': str(item)}
                                                 for item in set(map_data['Type'])],
                            multi=True,
                            value=list(set(map_data['Type']))
                        )
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                )
            ],
            className='row'
        ),

        # Map + table + Histogram
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(id='map-graph',
                                  animate=True,
                                  style={'margin-top': '20'})
                    ], className = "six columns"
                ),
                html.Div(
                    [
                        dt.DataTable(
                            rows=map_data.to_dict('records'),
                            columns=map_data.columns,
                            row_selectable=True,
                            filterable=True,
                            sortable=True,
                            selected_row_indices=[],
                            id='datatable'),
                    ],
                    style=layout_table,
                    className="six columns"
                ),
                html.Div([
                        dcc.Graph(
                            id='bar-graph'
                        )
                    ], className= 'twelve columns'
                    ),
            ], className="row"
        )
    ], className='ten columns offset-by-one'))

@app.callback(
    Output('map-graph', 'figure'),
    [Input('datatable', 'rows'),
     Input('datatable', 'selected_row_indices')])
def map_selection(rows, selected_row_indices):
    aux = pd.DataFrame(rows)
    temp_df = aux.ix[selected_row_indices, :]
    if len(selected_row_indices) == 0:
        return gen_map(aux)
    return gen_map(temp_df)

@app.callback(
    Output('datatable', 'rows'),
    [Input('type', 'value'),
     Input('boroughs', 'value')])
def update_selected_row_indices(tipo, bairro):
    map_aux = map_data.copy()

    # Type filter
    map_aux = map_aux[map_aux['Type'].isin(tipo)]
    # Boroughs filter
    map_aux = map_aux[map_aux["Borough"].isin(bairro)]

    rows = map_aux.to_dict('records')
    return rows

@app.callback(
    Output('bar-graph', 'figure'),
    [Input('datatable', 'rows'),
     Input('datatable', 'selected_row_indices')])
def update_figure(rows, selected_row_indices):
    dff = pd.DataFrame(rows)

    layout = go.Layout(
        bargap=0.05,
        bargroupgap=0,
        barmode='group',
        showlegend=False,
        dragmode="select",
        xaxis=dict(
            showgrid=False,
            nticks=50,
            fixedrange=False
        ),
        yaxis=dict(
            showticklabels=True,
            showgrid=False,
            fixedrange=False,
            rangemode='nonnegative',
            zeroline='hidden'
        )
    )

    data = Data([
         go.Bar(
             x=dff.groupby('Borough', as_index = False).count()['Borough'],
             y=dff.groupby('Borough', as_index = False).count()['Type']
         )
     ])

    return go.Figure(data=data, layout=layout)

#
# if __name__ == '__main__':
#     app.run_server()
