run:
	python main.py


test:
	pytest -s --cov-report xml --cov game tests