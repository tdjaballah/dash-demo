import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

gapminder = px.data.gapminder()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='This web application is built only with Python.'),

    dcc.Input(id='my-input', value='initial value', type='text'),

    html.Div(id='my-output'),

    dcc.Graph(
        id='example-graph',
        figure=px.line(gapminder[gapminder.continent == "Americas"], x="year", y="lifeExp", color='country')
    )

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
