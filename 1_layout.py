import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

gapminder = px.data.gapminder()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='This web application is built only with Python.'),

    dcc.Graph(
        id='example-graph',
        figure=px.line(gapminder[gapminder.continent == "Americas"], x="year", y="lifeExp", color='country')
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
