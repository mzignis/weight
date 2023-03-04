import plotly.graph_objects as go
from tools import get_records


def make_figure():
    _df_ = get_records()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=_df_['date'],
        y=_df_['weight'],
        mode='markers+lines'
    ))
    fig.update_xaxes(title='Date')
    fig.update_yaxes(title='Weight [kg]')

    return fig


if __name__ == '__main__':
    pass
