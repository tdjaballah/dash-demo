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

    dcc.Dropdown(
        id='selected-continent',
        options=[{'label': i, 'value': i} for i in list(gapminder.continent.unique())],
        value=gapminder.continent.iloc[0]
    ),

    dcc.Graph(id='my-graph')

])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='selected-continent', component_property='value')]
)
def update_output_div(selected_continent):
    return px.line(gapminder[gapminder.continent == selected_continent], x="year", y="gdpPercap", color='country')


if __name__ == '__main__':
    app.run_server(debug=True)
