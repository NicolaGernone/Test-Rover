setup:
	python -m venv env
	source env/bin/activate
	pip install -r requirements.txt

run:
	python main.py

lint:
	black .

profile:
	python -m cProfile -s cumtime main.py