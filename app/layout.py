import datetime

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from app.figure import make_figure


def make_modal():
    modal = dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Input data")),
            dbc.ModalBody([
                html.Div(dbc.Row('Select date')),
                dcc.DatePickerSingle(
                    id='input-date',
                    min_date_allowed=datetime.date(2020, 1, 1),
                    date=datetime.datetime.today().date()
                ),
                html.Br(),
                html.Br(),
                html.Div(dbc.Row('Type weight')),
                dcc.Input(
                    id="input-weight",
                    type="number",
                    placeholder="input weight",
                ),
                html.Br(),
                html.Br(),
            ]),
            dbc.ModalFooter(
                dbc.Row([
                    dbc.Col(
                        dbc.Button(
                            "Ok", id="ok", className="ms-auto", n_clicks=0
                        ),
                    ),
                    dbc.Col(
                        dbc.Button(
                            "Close", id="close", className="ms-auto", n_clicks=0
                        )
                    ),
                ], justify="end", className="g-1"),
            )
        ], id="modal", is_open=False,
    )

    return modal


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
                        dbc.Button("Add record", color="primary", id='open', n_clicks=0),
                        className="lead"
                    ),
                    html.P([], id='placeholder')
                ]),
                make_modal()
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
        html.Div(
            id='clicked-button',
            children='open:0 ok:0 close:0 last:nan',
            style={'display': 'none'}
        ),
    ])
    return layout


if __name__ == '__main__':
    pass
