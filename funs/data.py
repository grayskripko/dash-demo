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
    return pd.read_csv('data/covid.csv')\
        .assign(Date = lambda df: pd.to_datetime(df['Date']))
