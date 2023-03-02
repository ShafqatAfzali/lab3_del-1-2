import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly
import plotly.graph_objects as go
from collections import deque
import numpy as np
import pandas as pd
import random
from datetime import datetime


dt_format = '%Y-%m-%d %H:%M:%S.%f'
filnavn = './hist_mydaq.csv'

binST = 0.05
B = 3828
K = 0.0263
målt_Resistans = 10000
målt_Voltage = 5


def V_til_T(Uth_vektor):
    tt = B/np.log(Uth_vektor*målt_Resistans /
                  (K*(målt_Voltage-Uth_vektor)))-273.15
    return tt


X = deque(maxlen=1000)
X.append(1)

Y = deque(maxlen=1000)
Y.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1000,
            n_intervals=0
        ),
    ]
)


@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph_scatter(n):
    csv_data = pd.read_csv(filnavn)

    Y = V_til_T(csv_data["voltage"])
    X = list(
        map(lambda x: datetime.strptime(x, dt_format), csv_data['timestamp']))
    # Y = np.arange(start=X.min()-binST,
    #              stop=X.max()+binST, step=binST)

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='markers'
    )

    return {'data': [data],
            'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]), yaxis=dict(range=[min(Y), max(Y)]),)}


if __name__ == '__main__':
    app.run_server()
