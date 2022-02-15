# ML Template
A sample repo for structuring ML projects

## Setting up your local environment (in windows)

- Make sure to have [chocolatey](https://chocolatey.org/) installed
- Install Docker using `choco install docker-desktop`
- Install make using `choco install make`
- Have conda/anaconda installed
- run `make env` within the root directory of this project to create an empty environment
- Activate environment with `conda activate ml_template`
- install all dependencies by running `make deps` from the root directory of this project

## Making and merging branches

- run `git checkout main`, this will get you the main version of the code
- run `git pull origin main`, this will grab the latest main version from github.com
- run `git checkout -b <your_name>/<issue_number>` to create a new branch
- Make you changes to the code
- run `git add <file_name>` to add say you want to keep the changes
- run `git commit -m "<issue_number> : decription"` to create a snapshot of your updated code
- run `git push origin <branch_name>` to upload your code to github.com

## Running tests

- Run `make tests` to run unit test suite in the `./unittests` folder using pytest

## Using docker as a dev environment