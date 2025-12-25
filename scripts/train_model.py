"""Training script."""
import argparse
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from src.pipeline import SalesForecastingPipeline
from loguru import logger

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, required=True)
    parser.add_argument('--output', type=str, default='models/prophet_model.pkl')
    parser.add_argument('--periods', type=int, default=30)
    args = parser.parse_args()
    
    pipeline = SalesForecastingPipeline()
    pipeline.load_data(args.data)
    pipeline.preprocess()
    pipeline.train()
    forecast = pipeline.predict(periods=args.periods)
    metrics = pipeline.evaluate()
    pipeline.save_model(args.output)
    
    logger.info(f"Training complete. MAE: {metrics['mae']:.2f}")

if __name__ == '__main__':
    main()
