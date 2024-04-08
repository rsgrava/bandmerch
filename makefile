FLAGS := --onefile --noconsole --clean -n bandmerch
HIDDEN_IMPORTS := more_itertools appdirs

PYTHON_VERSION_FULL := $(wordlist 2,4,$(subst ., ,$(shell python --version 2>&1)))
PYTHON_VERSION := python$(word 1,$(PYTHON_VERSION_FULL)).$(word 2,$(PYTHON_VERSION_FULL))

ifeq ($(shell uname), Linux)
	ACTIVATE := source venv/bin/activate
else ifeq ($(OS), Windows_NT)
	ACTIVATE := ./venv/Scripts/activate
else
$(error Trying to build in unsupported OS. Please open an issue on github if you believe support should be added, or if you think this is a mistake)
endif

default: all

all: venv build clean

venv: 
	python -m venv ./venv
	$(ACTIVATE); \
	pip install -r requirements.txt

build:
	$(ACTIVATE); \
	pyside6-uic ui/main_window.ui -o src/ui_main_window.py; \
	pyinstaller $(FLAGS) $(foreach import, $(HIDDEN_IMPORTS), --hidden-import $(import)) --paths venv/lib/$(PYTHON_VERSION)/site-packages src/main.py

clean:
	@rm -rf build venv *.spec

lint:
	ruff check src

format:
	ruff format src
