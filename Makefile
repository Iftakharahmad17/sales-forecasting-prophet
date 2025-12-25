.PHONY: install test train

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/ -v

train:
	python scripts/train_model.py --data data/sample_sales_data.csv

predict:
	python scripts/predict.py --model models/prophet_model.pkl --periods 30
