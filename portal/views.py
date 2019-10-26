from django.shortcuts import render
import plotly.graph_objs as go
from plotly.offline import plot
import numpy as np



def home(request):

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

    template_name = 'portal/home.html'
    context = {
        'dash2': dashboard2(),
    }
    return render(request, template_name, context)