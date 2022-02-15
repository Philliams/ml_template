env_file ?= ./env.yaml
env_name ?= ml_template

env: 
	conda env remove -n ${env_name} # remove pre-existing conda env
	conda create --name ${env_name} python=3.8 # create new blank conda env

deps:
	python -m pip install flake8 pytest # install some dependencies for linting and testing
	pip install -r ./dependencies/requirements.txt # install project dependencies

test:
	python -m pytest --cov=src unittests/ # run pytest + code coverage

lint:
	flake8 src # lint the code

run:
	cd src && python main.py # run the main program