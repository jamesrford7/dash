# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
import pprint

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def configure_layout(graph_data):
    app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': graph_data,
                'layout': {
                    'title': 'Some cool TokenAnalyst data'
                }
            }
        )
    ])


if __name__ == '__main__':
    URL = "http://localhost:3000/api/single-metric"
    PARAMS = {
        'token': 'BTC',
        'window': '1d',
        'from_date': '2018-07-20',
        'to_date': '2019-10-30',
        'metric': 'Volume'
    }

    r = requests.get(url=URL, params=PARAMS)

    data = r.json()

    graph_data = [
        {'x': [x['date'] for x in data], 'y': [y['volume_real']
                                               for y in data], 'type': 'bar', 'name': 'Volume'}
    ]

    pprint.pprint(r.json())

    configure_layout(graph_data)
    app.run_server(debug=True)
