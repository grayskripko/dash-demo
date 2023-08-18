import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go


def main(df, y, countries):
    filtered_df = df[df['Country'].isin(countries)]
    
    # fig = go.Figure()
    fig = px.scatter(
        filtered_df, x='Date', y=y, color='Country', 
        labels={y: y.replace("_", " "), "Date": "Date"})
    fig.update_traces(mode='lines+markers')

            # marker=dict(size=5, opacity=0.5),
            # line=dict(width=2.5)))
        
    fig.update_layout(
        title={
            'text': "Covid, cases",
            'font': dict(size=24, family='Arial, bold'),
            'y':0.97, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'},
        autosize=True,
        margin=dict(l=15, r=15, b=15, t=50, pad=5) )
    
    
    # ylim = pd.Series([df[y].quantile(x) for x in [0.02, 0.98]])\
    #     .abs().mean().astype(int)
    # fig.update_yaxes(range=[-10, ylim])
    return fig
