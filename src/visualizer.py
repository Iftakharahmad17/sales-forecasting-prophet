"""Visualization utilities."""
import matplotlib.pyplot as plt
from loguru import logger

class ForecastVisualizer:
    def plot_forecast(self, model, forecast, figsize=(15, 6)):
        fig = model.plot(forecast, figsize=figsize)
        plt.title('Sales Forecast')
        return fig
    
    def plot_components(self, model, forecast):
        fig = model.plot_components(forecast)
        return fig
