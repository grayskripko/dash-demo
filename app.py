from datetime import datetime, timedelta
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from funs import plots, data
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.config.suppress_callback_exceptions = True
server = app.server  # Expose the server for the 'gunicorn' command
G = dict(data=data.get_data())


####
controls = dbc.Card([
    dbc.Row(id='y-axis-comp', children=[
        html.Label('Y axis'),
        dcc.Dropdown(
            id='plot-y', 
            options=[
                {'label': 'New cases', 'value': 'New_cases'},
                {'label': 'Cumulative cases', 'value': 'Cumulative_cases'}],
            value='New_cases', clearable=False)]),
    dbc.Row(id='countries-comp', children=[
        html.Label('Pick countries'),
        dcc.Dropdown(
            id='plot-countries', 
            options=G['data']['Country'].unique(),
            multi=True, value=['United States of America', 'China', 'India'], clearable=False)])
    ], body=True, 
    style={'margin': '45px 10px 10px 0px', "background-color": "#e7f7f5"})

app.layout = html.Div([
    dbc.Container([
        html.H3('Interactive Dashboard Demo', style={'margin': '30px 0px 10px 10px'}),
        dcc.Markdown('By Sergey Skripko', style={'margin': '20px 0px 0px 10px'}),
        dcc.Markdown('Please zoom in any region of the plot', style={'margin': '0px 0px 0px 10px'}),
        dbc.Row([
            dbc.Col([dcc.Graph(id='lineplots', figure=go.Figure())], md=10, xs=12),
            dbc.Col([controls], md=2, xs=12)
        ])
    ], fluid=True)
])

@app.callback(
    Output('lineplots', 'figure'),
    [Input('plot-y', 'value'),
     Input('plot-countries', 'value')])
def update_graph(plot_y, countries):
    return plots.main(G['data'], y=plot_y, countries=countries)

if __name__ == '__main__':
    app.run_server()


# az login
# - 1 prepare two system variables
# az webapp config set --resource-group dash-demo-rg --name skripko-demo --startup-file startup.txt
# az webapp config appsettings set --name skripko-demo --resource-group dash-demo-rg --settings SCM_DO_BUILD_DURING_DEPLOYMENT=1
# - 2 run
# az webapp up --name skripko-demo --resource-group dash-demo-rg
# az webapp up 
# - 3 logs, but with ~10 min delay. The docker, general and mostly useless, and default_docker
# https://skripko-demo.scm.azurewebsites.net/api/vfs/LogFiles/
# - 4 if az login is not successful, restart wsl --shutdown or, experimental:
# sudo hwclock -s
