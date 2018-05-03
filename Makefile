.PHONY: build

MODULE:=apistar_ponyorm

style: isort

isort:
	isort -y

flake8:
	flake8

test:
	pytest --cov $(MODULE) --cov-report term-missing --cov-fail-under=100

test-coverage:
	py.test  --cov $(MODULE) --cov-report term-missing --cov-report html


githook: flake8 style
	
push:
	git status
	git push origin --all
	git push origin --tags

	
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -rf .pytest_cache

