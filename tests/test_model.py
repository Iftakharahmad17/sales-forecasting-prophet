"""Test model."""
import pytest
import pandas as pd
import numpy as np
from src.model import SalesForecastModel

def test_model_init():
    model = SalesForecastModel()
    assert not model.is_fitted

def test_model_fit():
    dates = pd.date_range('2023-01-01', periods=100)
    df = pd.DataFrame({'ds': dates, 'y': np.random.randint(1000, 5000, 100)})
    model = SalesForecastModel()
    model.fit(df)
    assert model.is_fitted
