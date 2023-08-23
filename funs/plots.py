import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go


def main(df, y, countries):
    filtered_df = df[df['Country'].isin(countries)]\
        .rename(columns={'Cumulative_perc_pop': 'Cumulative % of population'})\
        .rename(columns=lambda x: x.replace("_", " "))
    
    fig = px.scatter(
        filtered_df, x='Date', y=y.replace("_", " "), color='Country', 
        hover_data = [
            'Country', 'Date', 'New cases', 'Cumulative cases', 
            'Cumulative % of population'])
    fig.update_traces(mode='lines+markers')
        
    fig.update_layout(
        title={
            'text': f"Covid, cases on {filtered_df['Date'].max().strftime('%d.%m.%Y')}",
            'font': dict(size=24, family='Arial, bold'),
            'y':0.97, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'},
        autosize=True,
        margin=dict(l=15, r=15, b=15, t=50, pad=5) )
    return fig
