"""Test pipeline."""
from src.pipeline import SalesForecastingPipeline

def test_pipeline_init():
    pipeline = SalesForecastingPipeline()
    assert pipeline is not None
