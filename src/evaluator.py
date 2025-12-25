"""Model evaluation."""
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
from loguru import logger

class ModelEvaluator:
    def evaluate(self, actual, forecast):
        merged = actual.merge(forecast[['ds', 'yhat']], on='ds', how='inner')
        
        metrics = {
            'mae': mean_absolute_error(merged['y'], merged['yhat']),
            'rmse': np.sqrt(mean_squared_error(merged['y'], merged['yhat'])),
            'mape': mean_absolute_percentage_error(merged['y'], merged['yhat']) * 100,
        }
        
        logger.info(f"MAE: {metrics['mae']:.2f}, RMSE: {metrics['rmse']:.2f}, MAPE: {metrics['mape']:.2f}%")
        return metrics
