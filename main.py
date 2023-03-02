import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go

from dash import html
from db import engine, DateWeightTable
from sqlalchemy.orm import Session

# -------- get data --------
with Session(engine) as session:
    df = pd.DataFrame(session.query(DateWeightTable.__table__).all())

# -------- dash app --------
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['date'], y=df['weight'], mode='markers+lines'))
fig.update_xaxes(title='Date')
fig.update_yaxes(title='Weight [kg]')

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Jumbotron", className="display-3"),
            html.P(
                "Use Containers to create a jumbotron to call attention to "
                "featured content or information.",
                className="lead",
            ),
            html.Div(
                dbc.Row([
                    dbc.Col(dash.dcc.Graph(figure=fig), width=9),
                    dbc.Col(
                        dash.dash_table.DataTable(df.to_dict('records')),
                        width=3
                    ),
                ])
            ),
            html.Hr(className="my-2"),
            html.P(
                "Use utility classes for typography and spacing to suit the "
                "larger container."
            ),
            html.P(
                dbc.Button("Learn more", color="primary"), className="lead"
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(jumbotron),
    ]),
])

if __name__ == "__main__":
    app.run_server(debug=True)
