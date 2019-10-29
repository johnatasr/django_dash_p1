from django.shortcuts import render
import plotly.graph_objs as go
from plotly.offline import plot
import numpy as np
import pandas as pd



def home(request):
    template_name = 'portal/home.html'
    return render(request, template_name)

def painel(request):

    def dashboard1():

        url = 'https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'
        df = pd.read_csv(url)

        # x, y = [], []

        # for pais in df['Country']:
        #     x.append(pais)
        #
        # for regiao in df['Region']:
        #     y.append(regiao)


        trace = go.Bar(x=df['Region'], y=df['Country'])
        layout = dict(title='Países')

        fig = go.Figure(data=[trace], layout=layout)

        plot_fig = plot(fig, output_type='div', include_plotlyjs=True)

        return plot_fig

    def dashboard2():
        x = np.random.randint(1, 100, 100)
        y = np.random.randint(1, 100, 100)

        trace = go.Scatter(x=x, y=y, mode='markers')
        layout = dict(title='Outro Gráfico',
                      xaxis=dict(range=[min(x), max(x)]),
                      yaxis=dict(range=[min(y), max(y)]))
        fig = go.Figure(data=[trace], layout=layout)
        plot_fig = plot(fig, output_type='div', include_plotlyjs=False)

        return plot_fig

    def rosca():

        labels = ['Oxigenio', 'Hidrogenio', 'CO2', 'Nitrogenio']
        values = [4500, 2500, 1053, 500]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

        plot_fig = plot(fig, output_type='div', include_plotlyjs=True)

        return plot_fig

    template_name = 'portal/painel.html'

    context = {
        'plot1': dashboard1,
        'plot2': rosca,
        'plot3': dashboard2,
    }

    return render(request, template_name, context)

