import datetime

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from app.figure import make_figure


def make_jumbotron():
    jumbotron = html.Div(
        dbc.Container(
            [
                html.H1("Weight monitor", className="display-3"),
                html.P(
                    "Simple Plotly app to monitor my weight",
                    className="lead",
                ),
                html.Div(
                    dbc.Row([
                        dbc.Col(dash.dcc.Graph(id='graph', figure=make_figure())),
                    ])
                ),
                html.Hr(className="my-2"),
                html.Div([
                    html.P(
                        "Insert new record"
                    )
                ]),
                html.Div([
                    dbc.Row([
                        dbc.Col(
                            dcc.DatePickerSingle(
                                id='input-date',
                                min_date_allowed=datetime.date(2020, 1, 1),
                                date=datetime.datetime.today().date()
                            )
                        )
                    ]),
                    dbc.Row([
                        dbc.Col(
                            dcc.Input(
                                id="input-weight",
                                type="number",
                                placeholder="input weight",
                            )
                        )
                    ])
                ]),
                html.Br(),
                html.Div([
                    html.P(
                        dbc.Button("Learn more", color="primary", id='my-input'), className="lead"
                    ),
                    html.P([], id='placeholder')
                ]),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-light rounded-3",
    )

    return jumbotron


def make_layout():
    layout = dbc.Container([
        dbc.Row([
            dbc.Col(make_jumbotron()),
        ]),
    ])
    return layout


if __name__ == '__main__':
    pass
