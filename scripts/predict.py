"""Prediction script."""
import argparse
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from src.model import SalesForecastModel
from loguru import logger

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, required=True)
    parser.add_argument('--periods', type=int, default=30)
    parser.add_argument('--output', type=str, default='reports/forecast.csv')
    args = parser.parse_args()
    
    model = SalesForecastModel()
    model.load_model(args.model)
    forecast = model.predict(periods=args.periods)
    
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    forecast.to_csv(args.output, index=False)
    logger.info(f"Forecast saved to {args.output}")

if __name__ == '__main__':
    main()
