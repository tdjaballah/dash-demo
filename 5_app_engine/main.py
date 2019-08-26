import dash
import dash_core_components as dcc
import dash_html_components as html
import json
import plotly.express as px

from dash.dependencies import Input, Output
from textwrap import dedent as d

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}


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

    dcc.Graph(id='my-graph'),

    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown(d("""
                **Hover Data**

                Mouse over values in the graph.
            """)),
            html.Pre(id='hover-data', style=styles['pre'])
        ], className='four columns'),

        html.Div([
            dcc.Markdown(d("""
                **Click Data**

                Click on points in the graph.
            """)),
            html.Pre(id='click-data', style=styles['pre']),
        ], className='four columns'),

        html.Div([
            dcc.Markdown(d("""
                **Zoom and Relayout Data**

                Click and drag on the graph to zoom or click on the zoom
                buttons in the graph's menu bar.
                Clicking on legend items will also fire
                this event.
            """)),
            html.Pre(id='relayout-data', style=styles['pre']),
        ], className='four columns')
    ])

])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='selected-continent', component_property='value')]
)
def update_output_div(selected_continent):
    return px.line(gapminder[gapminder.continent == selected_continent], x="year", y="gdpPercap", color='country')


@app.callback(
    Output('hover-data', 'children'),
    [Input('my-graph', 'hoverData')])
def display_hover_data(hover_data):
    return json.dumps(hover_data, indent=2)


@app.callback(
    Output('click-data', 'children'),
    [Input('my-graph', 'clickData')])
def display_click_data(click_data):
    return json.dumps(click_data, indent=2)


@app.callback(
    Output('relayout-data', 'children'),
    [Input('my-graph', 'relayoutData')])
def display_selected_data(relayout_data):
    return json.dumps(relayout_data, indent=2)


if __name__ == '__main__':
    app.run_server(debug=True)
