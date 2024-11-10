# Motion Detection Project

This project uses OpenCV to detect motion by comparing consecutive frames from the webcam feed.

## Setup

You need Python 3.7+ and `Poetry` to manage dependencies.

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
poetry run python motion_detection.py
