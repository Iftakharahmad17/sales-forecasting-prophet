"""Test preprocessor."""
import pytest
import pandas as pd
import numpy as np
from src.preprocessor import SalesDataPreprocessor

def test_convert_dates():
    df = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02'],
        'sales': [100, 200]
    })
    prep = SalesDataPreprocessor()
    result = prep.convert_dates(df)
    assert pd.api.types.is_datetime64_any_dtype(result['date'])
