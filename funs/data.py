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
    data_url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
    return pd.read_csv(data_url)\
        .assign(Date = lambda df: pd.to_datetime(df['Date_reported']))
