import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly.express as px
from collections import deque
import numpy as np
import pandas as pd
import random
from datetime import datetime


dt_format = '%Y-%m-%d %H:%M:%S.%f'
filnavn = 'hist_mydaq.csv'

binST = 0.05
B = 3828
K = 0.0263
målt_Resistans = 10000
målt_Voltage = 5


def V_til_T(Uth_vektor):
    tt = B/np.log(Uth_vektor*målt_Resistans /
                  (K*(målt_Voltage-Uth_vektor)))-273.15
    return tt


X = deque(maxlen=20)
X.append(1)

Y = deque(maxlen=20)
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

    X = V_til_T(csv_data["voltage"])
    temp_frame = np.histogram(X)
    # Y = np.arange(start=X.min()-binST,
    #              stop=X.max()+binST, step=binST)
    # binner_frame = pd.DataFrame(Y)

    fig = px.histogram(temp_frame, height=600,
                       width=900, text_auto=True, color_discrete_sequence=["red"], template="plotly_dark")

    return fig


if __name__ == '__main__':
    app.run_server()
