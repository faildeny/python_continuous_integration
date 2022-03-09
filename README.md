# Python Continuous Integration example
![Continuous integration](https://github.com/faildeny/python_continuous_integration/actions/workflows/python-ci.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This is a sample python app that performs basic CI workflow based on GitHub Actions.

 This GitHub Action workflow will

 - Format imports using isort
 - Format code using Black
 - Commit formatting changes
 - Build project with all dependencies
 - Check code with flake8 linter
 - Run tests with pytest

See this repository's
 [Actions](https://github.com/faildeny/python_continuous_integration/actions/workflows/python-ci.yml)

## Commiting changes during GitHub Action
### Why?
This step involved much more work and that's mostly why this repo was created. Code formatting may be approached in different ways for example (pre commit git hook). But in some situations it may be more convenient to reformat code independent of the commiters setup. 

### Details
The action will commit and push formatting changes to the repo with message: 'Fix styling'.
The commit hash is saved and used for checkout in the next workflow stages like linting. This is not the default behaviour in GitHub Actions, as it will normally omit any changes that happened during the GitHub Action.

## Executed workflow commands

### Isort formatting
```isort --profile black .```
this ensures that Isort and Black formatting rules are as close are possible
### Black formatting
```black .```
### App build
```pip install .```
### Flake8 linting
```flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --max-line-length=88 --extend-ignore=E203,E501```
line length adjusted to Black formatting standards

### Pytest testing
```pytest```

## Commit and push in GitHub Action:
```
formatting:
    outputs:
      new_sha: ${{ steps.sha.outputs.SHA }}
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2
        with:
          ref: ${{ github.event.pull_request.head.ref }}

      - name: Setup Python 3.8
        uses: actions/setup-python@v2
        with:
          python-version: "3.8"
          cache: 'pip'

      - name: Setup isort and Black
        run: |
          python -m pip install --upgrade pip
          pip install isort black

      - name: Run isort
        run: |
          isort --profile black .

      - name: Run Black formatter
        run: |
          black .

      - name: Commit changes
        uses: EndBug/add-and-commit@v8
        with:
          message: 'Fix styling'
          add: '*.py'
      
      - name: Get commit hash
        id: sha
        run: |
          sha_new=$(git rev-parse HEAD)
          echo $sha_new
          echo "::set-output name=SHA::$sha_new"
```

## Checkout to code modified in GitHub Action:
```
build:
    if: always()
    needs: formatting
    runs-on: ubuntu-latest

    steps:
    - name: Checkout to latest changes
      uses: actions/checkout@v2
      with:
        ref: ${{ needs.formatting.outputs.new_sha }}
        fetch-depth: 0
```

## Status Badges
- Continuous integration ![Continuous integration](https://github.com/faildeny/python_continuous_integration/actions/workflows/python-ci.yml/badge.svg)


    ```![Continuous integration](https://github.com/user_name/repository_name/actions/workflows/python-ci.yml/badge.svg)```

- Black formatting [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

    ```[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)```
