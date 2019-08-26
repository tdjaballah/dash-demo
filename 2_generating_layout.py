import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

gapminder = px.data.gapminder()


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='This web application is built only with Python.'),

    dcc.Graph(
        id='example-graph',
        figure=px.line(gapminder[gapminder.continent == "Europe"], x="year", y="gdpPercap", color='country')),

    generate_table(gapminder)

    ])


if __name__ == '__main__':
    app.run_server(debug=True)
