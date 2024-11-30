# Motion Detection Project

This project uses OpenCV to detect motion by comparing consecutive frames from the webcam feed.

## Setup

You need Python 3.11+ and `Poetry` to manage dependencies.

1. Install Poetry (if not already installed):
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

## Running the Project

After installing the dependencies, you can run the motion detection script:

```bash
poetry install
```

### Additional features to debug, log, test, profile, analyze your software

## Static Code Analysis with Flake8
To ensure code quality, this project uses [Flake8](https://flake8.pycqa.org/) for static code analysis.  

### Installation
Flake8 is already included in the project's dependencies. You can install it by running:
```bash
poetry install
```

### To run analysis
Use this command :
```bash
poetry run flake8
```


## Automating Code Analysis with Pre-commit Hooks
This project uses [pre-commit](https://pre-commit.com/) to automate code quality checks before committing changes.  

### Installation
Pre-commit is included in the development dependencies. To install and activate the hooks, run:
```bash
poetry install
poetry run pre-commit install
```
