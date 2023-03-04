import dash
import dash_bootstrap_components as dbc

from app.layout import make_layout
from app.callbacks import get_callbacks

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = make_layout
get_callbacks(app)
