import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Some inputs and callback Dash examples'),

    html.Div(children='This web application is built only with Python.'),

    dcc.Input(id='my-input-1', value='initial value', type='text'),

    html.Div(id='my-output-1'),

    dcc.Checklist(
        id='my-input-2',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),

    html.Div(id='my-output-2')

])


@app.callback(
    Output(component_id='my-output-1', component_property='children'),
    [Input(component_id='my-input-1', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}" with type {}.'.format(input_value, type(input_value))


@app.callback(
    Output(component_id='my-output-2', component_property='children'),
    [Input(component_id='my-input-2', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}" with type {}.'.format(input_value, type(input_value))


if __name__ == '__main__':
    app.run_server(debug=True)
