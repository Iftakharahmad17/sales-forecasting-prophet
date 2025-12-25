"""Data loading utilities."""
import pandas as pd
from pathlib import Path
from loguru import logger

class DataLoader:
    def __init__(self, date_column='date', target_column='sales'):
        self.date_column = date_column
        self.target_column = target_column
    
    def load_csv(self, filepath):
        logger.info(f"Loading data from {filepath}")
        df = pd.read_csv(filepath)
        logger.info(f"Loaded {len(df)} rows")
        return df
    
    def validate_data(self, df):
        required = [self.date_column, self.target_column]
        missing = [col for col in required if col not in df.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")
        return True
    
    def load_and_validate(self, filepath):
        df = self.load_csv(filepath)
        self.validate_data(df)
        return df
