import dash

from tools import insert_record
from app.figure import make_figure


def get_callbacks(app):
    @app.callback(
        dash.Output('modal', 'is_open'),
        [dash.Input('clicked-button', 'children')],
        [dash.State("modal", "is_open")]

    )
    def on_clicked_button(clicked, is_open):
        last_clicked = clicked.split(' ')[-1][5:]
        if last_clicked == 'open' or last_clicked == 'close':
            return not is_open
        elif last_clicked == 'ok':
            return not is_open
        else:
            return is_open

    @app.callback(
        dash.Output("clicked-button", "children"),
        [dash.Input("open", "n_clicks"), dash.Input("ok", "n_clicks"), dash.Input("close", "n_clicks")],
        [dash.State('clicked-button', 'children')]
    )
    def on_open_ok_close_clicked(open_clicks, ok_clicks, close_clicks, prev_clicks):
        prev_clicks = dict([i.split(':') for i in prev_clicks.split(' ')])
        last_clicked = 'nan'

        if open_clicks > int(prev_clicks['open']):
            last_clicked = 'open'
        elif ok_clicks > int(prev_clicks['ok']):
            last_clicked = 'ok'
        elif close_clicks > int(prev_clicks['close']):
            last_clicked = 'close'

        cur_clicks = f'open:{open_clicks} ok:{ok_clicks} close:{close_clicks} last:{last_clicked}'

        return cur_clicks

    @app.callback(
        dash.Output('graph', 'figure'),
        [dash.Input('clicked-button', 'children')],
        [dash.State('input-date', 'date'), dash.State('input-weight', 'value')]

    )
    def update_output_div(clicked, input_date, input_weight):
        last_clicked = clicked.split(' ')[-1][5:]
        if last_clicked == 'ok' and input_date and input_weight:
            insert_record(input_date, input_weight)
            print(f'add new record {input_date}, {input_weight}')

        return make_figure()


if __name__ == '__main__':
    pass
