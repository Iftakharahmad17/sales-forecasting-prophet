"""Data preprocessing."""
import pandas as pd
import numpy as np
from loguru import logger

class SalesDataPreprocessor:
    def __init__(self, date_column='date', target_column='sales'):
        self.date_column = date_column
        self.target_column = target_column
    
    def convert_dates(self, df):
        df = df.copy()
        df[self.date_column] = pd.to_datetime(df[self.date_column])
        return df
    
    def handle_missing_values(self, df, method='interpolate'):
        df = df.copy()
        if df[self.target_column].isna().sum() > 0:
            if method == 'interpolate':
                df[self.target_column] = df[self.target_column].interpolate()
        return df
    
    def aggregate_daily_sales(self, df):
        return df.groupby(self.date_column)[self.target_column].sum().reset_index()
    
    def prepare_for_prophet(self, df):
        df_prophet = df[[self.date_column, self.target_column]].copy()
        df_prophet.columns = ['ds', 'y']
        return df_prophet
    
    def preprocess(self, df):
        logger.info("Preprocessing data")
        df = self.convert_dates(df)
        df = self.handle_missing_values(df)
        df = self.aggregate_daily_sales(df)
        df = self.prepare_for_prophet(df)
        logger.info("Preprocessing complete")
        return df
