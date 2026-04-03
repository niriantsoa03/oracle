CWD=$(shell pwd)
PYTHON=${CWD}/.venv/bin/python3
PIP=${CWD}/.venv/bin/pip3

cls:
	clear

init:
	@python3 -m venv .venv
	@${PIP} install -r requirements.txt 

run: cls
	@${PYTHON} ./plotter.py ../data/sample.csv
