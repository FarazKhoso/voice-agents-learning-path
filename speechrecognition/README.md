# Speech Recognition Example

This project demonstrates how to perform speech recognition in Python using the `SpeechRecognition` library. It captures audio from the microphone and uses Google's Web Speech API to convert the speech to text.

## How it Works

The `main.py` script listens for audio from the microphone, sends it to Google's Web Speech API for recognition, and prints the recognized text to the console.

## Setup and Usage

1.  **Install Dependencies:**
    
    Install the required Python libraries using the `requirements.txt` file:
    
    ```bash
    pip install -r requirements.txt
    ```
    
    *Note: `PyAudio` is required for microphone access. If you encounter issues during its installation, you may need to install it using a wheel file or through a system package manager like `brew` or `apt`.*
    
2.  **Run the script:**
    
    ```bash
    python main.py
    ```
    
    The script will adjust for ambient noise and then start listening. Speak into your microphone, and the recognized text will be displayed.
    
3.  **Exit the program:**
    
    Press `Ctrl+C` to stop the script.
    
## Requirements

*   Python 3.x
*   An active internet connection (for Google's Web Speech API)
*   A microphone connected to your computer

