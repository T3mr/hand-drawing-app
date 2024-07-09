# Hand Drawing Application with OpenCV and MediaPipe

This project is a simple hand drawing application that allows users to draw on a canvas using their hands. The application uses OpenCV and MediaPipe to detect hand movements and draw lines based on the position of the user's index finger.

## Features

- **Real-time Hand Tracking:** Uses MediaPipe to track the user's hand and index finger in real-time.
- **Drawing:** Draw on the canvas by moving your index finger.
- **Color Selection:** Switch between different colors using on-screen buttons.
- **Clear Canvas:** Clear the entire canvas with a single button.
- **Toggle Drawing Mode:** Turn drawing mode on and off.
- **Exit Application:** Exit the application using the 'ESC' or 's' key.

## Requirements

- Python 3.6+
- OpenCV
- MediaPipe
- NumPy

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/hand-drawing-application.git
    cd hand-drawing-application
    ```

2. **Create a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required libraries:**

    ```sh
    pip install opencv-python mediapipe numpy
    ```

## Usage

Run the application:

```sh
python hand-drawing-app.py
