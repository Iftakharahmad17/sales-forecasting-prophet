"""Prophet model wrapper."""
import pandas as pd
from prophet import Prophet
import pickle
from pathlib import Path
from loguru import logger

class SalesForecastModel:
    def __init__(self):
        self.model = Prophet(
            seasonality_mode='multiplicative',
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=False
        )
        self.is_fitted = False
    
    def fit(self, df):
        logger.info("Training model")
        self.model.fit(df)
        self.is_fitted = True
    
    def predict(self, periods=30):
        if not self.is_fitted:
            raise ValueError("Model not fitted")
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast
    
    def save_model(self, filepath):
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'wb') as f:
            pickle.dump(self.model, f)
        logger.info(f"Model saved to {filepath}")
    
    def load_model(self, filepath):
        with open(filepath, 'rb') as f:
            self.model = pickle.load(f)
        self.is_fitted = True
