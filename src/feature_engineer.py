"""Feature engineering."""
import pandas as pd
from loguru import logger

class FeatureEngineer:
    def add_date_features(self, df):
        df = df.copy()
        df['day_of_week'] = df['ds'].dt.dayofweek
        df['month'] = df['ds'].dt.month
        df['quarter'] = df['ds'].dt.quarter
        df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
        return df
    
    def add_features(self, df):
        logger.info("Engineering features")
        return self.add_date_features(df)
