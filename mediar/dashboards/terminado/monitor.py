from dash.dependencies import Output, Input
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pyodbc
# from ...conexao import mediar_data
from django.db import connections, Error
import pandas as pd
import numpy as np

# def mediar_data(self):
#     with connections['BaseMediar'].cursor() as cursor:
#         try:
#             cursor.execute('''select * from monitoring_logportal a
#                             inner join [dbo].[auth_user] b
#                             on a.fk_usuario_id = b.id
#                             where is_superuser = 0
#                             and username not in('demo_brasil', 'CONTROLE', 'Mediar_Testes', 'Mediar_Ingles')''')
#             rows = cursor.fetchall()
#             return rows
#         except Error as e:
#             sqlstate = e.args[0]
#             if sqlstate == '28000':
#                 print('Erro de senha !')

def mediar_data():
    conn = pyodbc.connect(
        'Driver={ODBC Driver 13 for SQL Server};' \
        'Server=10.177.51.52,49318;' \
        'Database=PortalMediar;' \
        'Uid=sa;' \
        'Pwd=jm#srv@1!v2;'
    )
    linhas =[]

    cursor = conn.cursor()
    cursor.execute('''select * from monitoring_logportal a
                                 inner join [dbo].[auth_user] b
                                 on a.fk_usuario_id = b.id
                                 where is_superuser = 0
                                 and username not in('demo_brasil', 'CONTROLE', 'Mediar_Testes', 'Mediar_Ingles')''')

    result = cursor.fetchall()

    data = [dict((cursor.description[i][0], value) for i, value in enumerate(row))for row in result]

    cursor.close()

    return data

data = mediar_data()



#
# app = DjangoDash('MediarMonitor')
#
# data = []
# base = mediar_data()
#
# data.append(base)
#
# dropdowns = [
#     'teste1',
#     'teste2'
# ]
#
# trace1 = [go.Bar(x=0,y=0,)]
#
#
# app.layout = html.Div([
#         html.Div([
#             html.Img(id='header')
#         ]),
#         html.Div([
#             dcc.Dropdown(id='ano', options=dropdowns),
#             dcc.Dropdown(id='mes', options=dropdowns),
#             dcc.Dropdown(id='dia'),
#             dcc.Dropdown(id='hora'),
#             dcc.Dropdown(id='usuario'),
#             dcc.Dropdown(id='mais_acesso'),
#             dcc.Dropdown(id='t_acessos')
#         ]),
#         html.Div([
#             dcc.Tab(id='table'),
#             dcc.Graph(id='a_periodo', figure=)
#         ]),
#         html.Div([
#            dcc.Graph(id='a_usuario'),
#            dcc.Graph(id='a_hora')
#         ])
#
# ])
# @app.callback(Output('a_periodo', 'figure'),
#               [Input('ano', 'value')])
# def callback_dropdows_ano(ano):
#     while ano == '2019':
#         format(12,)
#         pass


# def callback_dropdows_mes(mes):
# def callback_dropdows_dia(dia):
# def callback_dropdows_hora(hora):
# def callback_dropdows_usuario(usuario):
# def callback_dropdows_mais_acesso(mais_acesso):
# def callback_dropdows_t_acesso(t_acesso):
# def callback_dropdows(ano, mes, dia, hora, usuario, mais_acesso, t_acesso):
#     pass
# def callback_table(usuario, qntd, acessos):
#     pass
#
# def callback_periodo():
#     pass