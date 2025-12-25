"""Anomaly detection."""
import pandas as pd
import numpy as np
from scipy import stats
from loguru import logger

class AnomalyDetector:
    def __init__(self, method='zscore'):
        self.method = method
    
    def detect_zscore(self, df, threshold=3.0):
        z_scores = np.abs(stats.zscore(df['y']))
        anomalies = df[z_scores > threshold].copy()
        return anomalies
    
    def detect(self, df):
        if self.method == 'zscore':
            return self.detect_zscore(df)
        return pd.DataFrame()
