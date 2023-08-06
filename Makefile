# Define the python environment and the main script you want to profile
PYTHON = .venv/bin/python3
SCRIPT = main.py
SRC = src

# Create a virtual environment
setup:
	python3 -m venv .venv
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -r requirements/requirements.txt

# Profile memory usage
memory-profile:
	$(PYTHON) -m memory_profiler $(SCRIPT)

# Profile execution time of individual lines
line-profile:
	$(PYTHON) -m kernprof -l -o $(SRC)/$(SCRIPT).lprof $(SRC)/$(SCRIPT)
	$(PYTHON) -m line_profiler $(SRC)/$(SCRIPT).lprof

# Profile execution time
profile:
	$(PYTHON) -m cProfile -s cumtime $(SRC)/$(SCRIPT)

# Run the script
run:
	$(PYTHON) $(SRC)/$(SCRIPT)

# Run tests
test:
	$(PYTHON) -m pytest $(SRC)/tests/

# Reformat code
lint:
	black .

# Measure code coverage
coverage:
	$(PYTHON) -m pytest --cov-report term --cov=$(SRC)

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf $(SRC)/*.lprof

.PHONY: setup memory-profile line-profile run test coverage clean
