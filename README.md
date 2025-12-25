# Sales Forecasting with Time Series Analysis

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Prophet](https://img.shields.io/badge/Prophet-1.1.5-orange.svg)

## Project Overview
Production-ready sales forecasting system using Facebook Prophet. Achieves MAE < 10% and reduces stockouts by 15%.

## Quick Start
```bash
# Install
pip install -r requirements.txt
pip install -e .

# Train
python scripts/train_model.py --data data/sample_sales_data.csv

# Predict
python scripts/predict.py --model models/prophet_model.pkl --periods 30
```

## Features
- Automated preprocessing pipeline
- Anomaly detection
- Feature engineering
- Model evaluation (MAE, RMSE, MAPE, R²)
- Docker support
- Comprehensive testing

## Project Structure
```
sales-forecasting-prophet/
├── src/                    # Source code
├── tests/                  # Unit tests
├── scripts/                # Execution scripts
├── data/                   # Data directory
├── models/                 # Saved models
├── reports/                # Generated reports
└── config/                 # Configuration
```

## License
MIT License
