import dash

from tools import insert_record
from app.figure import make_figure


def get_callbacks(app):
    @app.callback(
        dash.Output('graph', 'figure'),
        dash.Input('my-input', 'n_clicks'),
        dash.State('input-date', 'date'),
        dash.State('input-weight', 'value')

    )
    def update_output_div(input_value, input_date, input_weight):
        if input_value and input_date and input_weight:
            insert_record(input_date, input_weight)
            print(f'add new record {input_date}, {input_weight}')

        return make_figure()


if __name__ == '__main__':
    pass
