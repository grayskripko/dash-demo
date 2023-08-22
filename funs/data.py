import os
import time
import pandas as pd
import numpy as np
from pandas.tseries.offsets import MonthBegin
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from datetime import datetime


def get_data():
    pop = pd.read_csv('data/population.csv').set_index('Country').squeeze() * 1e6
    data_url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
    return pd.read_csv(data_url)\
        .assign(Date = lambda df: pd.to_datetime(df['Date_reported']))\
        .assign(pop = lambda d: d['Country'].map(pop))\
        .assign(Cumulative_perc_pop = lambda d: (100 * d['Cumulative_cases'] / d['pop'])\
                .replace([np.inf, -np.inf, np.nan], 0).round(2))
