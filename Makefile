.PHONY: build

MODULE:=apistar_ponyorm.py

all: dev style checks requirements.txt  build dists test-unit test-coverage

dev:
	pipenv install --dev --python 3.6 --skip-lock

install-local:
	pipenv install --python 3.6

install-system:
	pipenv install --system

style: isort autopep8 yapf

isort:
	pipenv run isort -y

autopep8:
	pipenv run autopep8 --in-place --recursive setup.py $(MODULE)

yapf:
	pipenv run yapf --recursive -i $(MODULE)

checks:
	pipenv check

flake8:
	pipenv run python setup.py flake8

build: dists

shell:
	pipenv shell

test-unit:
	pipenv run pytest --cov $(MODULE) --cov-report term-missing --cov-fail-under=100

test-coverage:
	pipenv run py.test  --cov $(MODULE) --cov-report term-missing --cov-report html

requirements.txt:
	
	# generate requirements.txt from Pipfile
	# needed until PBR supports `Pipfile`
	pipenv run pipenv_to_requirements
	
	

Pipfile.lock:	Pipfile
	pipenv lock

dists: requirements.txt sdist wheels

sdist:
	pipenv run python setup.py sdist

wheels:
	pipenv run python setup.py bdist_wheel

deploy: build
	 pipenv run twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

update:
	pipenv update -d

githook: checks style requirements.txt
	
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



# aliases to gracefully handle typos on poor dev's terminal
check: checks
devel: dev
develop: dev
dist: dists
install: install-system
pypi: pypi-publish
styles: style
test: test-unit
unittest: test-unit
wheel: wheels
