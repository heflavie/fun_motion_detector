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



## Logging Configuration
This project uses Python's built-in logging module to track important events during execution. Logs provide valuable information for debugging and monitoring the behavior of the motion detection system.

### Log Levels
- **DEBUG**: Logs detailed internal states, such as the calculated frame differences. These logs are useful for debugging and understanding how the system processes video frames.
- **INFO**: Regular information on the state of the program (e.g., initialization, motion detection events, system shutdown).
- **WARNING**: A warning when no significant motion is detected in a frame, indicating that the system is not detecting relevant changes.
- **ERROR**: Indicates errors such as failure to open the camera or capture frames.

### Viewing Logs
Logs will be printed to the console by default. You can configure logging to write to a file by modifying the `logging.basicConfig` in the code. Ensure that your IDE or terminal is configured to display log messages for debugging.

