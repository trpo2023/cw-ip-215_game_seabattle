all: run

run: test
	python main.py
test:
	python test_main.py
