"""Evaluation script."""
import argparse
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from src.pipeline import SalesForecastingPipeline
from loguru import logger

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, required=True)
    parser.add_argument('--data', type=str, required=True)
    args = parser.parse_args()
    
    pipeline = SalesForecastingPipeline()
    pipeline.load_model(args.model)
    pipeline.load_data(args.data)
    pipeline.preprocess()
    forecast = pipeline.predict(periods=0)
    metrics = pipeline.evaluate()
    
    print(f"\nMAE: {metrics['mae']:.2f}")
    print(f"RMSE: {metrics['rmse']:.2f}")
    print(f"MAPE: {metrics['mape']:.2f}%")

if __name__ == '__main__':
    main()
