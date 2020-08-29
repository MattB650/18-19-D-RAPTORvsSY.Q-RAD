import os
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input



styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

sheet = pd.read_csv('FIN Best Lineup D-RAPTOR vs SY Q-RAD.csv', index_col=0)


abs_bubble_size = abs(sheet['AVG D-RAPTOR'])
sheet['ABS D-RAPTOR'] = abs_bubble_size

fig = px.scatter(sheet, x='AVG SY Q-RAD', y='AVG D-RAPTOR', color='ABS D-RAPTOR', title= '2018-19 5 Man SY Q-RAD vs D-RAPTOR',
                 hover_name='Team', hover_data=['Lineup', 'AVG SY Q-RAD', 'AVG D-RAPTOR'])

fig.update_traces(mode='markers', marker_size=27)

fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    )
)















external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure=fig
    ),

    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown("""
                **Hover Data**
                Mouse over a point to reveal team and lineup.
            """),
            html.Pre(id='hover-data', style=styles['pre'])
        ], className='three columns'),
        
        html.Div([
            dcc.Markdown("""
                **Description**
            
                This plot includes the best 5-man lineup (min. 100
                possessions played, per CleaningTheGlass) from each
                2018-19 NBA team. The two metrics used are D-RAPTOR
                (per FiveThirtyEight) and SY Q-RAD (per Andrew Patton
                and B-Ball Index), with the latter looking at how
                much on average a defender deterrs an offensive player
                from attempting high efficiency shots (corner threes,
                layups, etc.). This plot aims to provide an alternative
                way to measure team defense.
                """),
                html.Pre(id='description', style=styles['pre'])
            ], className='three columns')
        ])
    ])



if __name__ == '__main__':
    app.run_server()










