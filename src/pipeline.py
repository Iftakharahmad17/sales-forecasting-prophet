"""End-to-end pipeline."""
from pathlib import Path
from loguru import logger
from src.data_loader import DataLoader
from src.preprocessor import SalesDataPreprocessor
from src.anomaly_detector import AnomalyDetector
from src.feature_engineer import FeatureEngineer
from src.model import SalesForecastModel
from src.evaluator import ModelEvaluator
from src.visualizer import ForecastVisualizer

class SalesForecastingPipeline:
    def __init__(self, config_path=None):
        self.loader = DataLoader()
        self.preprocessor = SalesDataPreprocessor()
        self.anomaly_detector = AnomalyDetector()
        self.feature_engineer = FeatureEngineer()
        self.model = SalesForecastModel()
        self.evaluator = ModelEvaluator()
        self.visualizer = ForecastVisualizer()
        self.data = None
        self.processed_data = None
        self.forecast = None
    
    def load_data(self, filepath):
        self.data = self.loader.load_and_validate(filepath)
    
    def preprocess(self):
        self.processed_data = self.preprocessor.preprocess(self.data)
    
    def train(self):
        self.model.fit(self.processed_data)
    
    def predict(self, periods=30):
        self.forecast = self.model.predict(periods=periods)
        return self.forecast
    
    def evaluate(self):
        return self.evaluator.evaluate(self.processed_data, self.forecast)
    
    def save_model(self, filepath):
        self.model.save_model(filepath)
    
    def load_model(self, filepath):
        self.model.load_model(filepath)
