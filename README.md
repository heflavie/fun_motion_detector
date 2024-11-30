# Fun Motion Detector

## Description
This project uses the camera to detect motion by comparing consecutive video frames in real time. When significant motion is detected, a humorous alert message appears on the video feed.

## Installation
To manage dependencies and build, install [Poetry](https://python-poetry.org/). After installing Poetry, install the project's dependencies with:

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