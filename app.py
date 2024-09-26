from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html

# Create the Flask app
server = Flask(__name__)

# Create the Dash app
app = dash.Dash(__name__, server=server, url_base_pathname='/dash/')

# Define the Dash layout
app.layout = html.Div(children=[
    html.H1('Simple Dash App Inside Flask'),
    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

# Flask route for home page
@server.route('/')
def index():
    return 'Hello, Flask! Go to /dash/ to see the dashboard.'

# Run the app
if __name__ == '__main__':
    server.run(debug=True)

