# Python Text-to-Speech (TTS) Example using gTTS

This project is a simple demonstration of how to convert text into speech in Python using the `gTTS` (Google Text-to-Speech) library. It also uses the `pydub` library to play the generated audio.

This project is intended for students and beginners who want to learn how to work with text-to-speech in Python.

## How it Works

The script `main.py` performs the following steps:

1.  **Text to Speech Conversion:** It takes a sample text string.
2.  **gTTS Library:** It uses the `gTTS` library to send this text to the Google Text-to-Speech API.
3.  **Save Audio File:** The API returns an audio file (in MP3 format), which is saved as `output.mp3`.
4.  **Playback:** The `pydub` library is used to load and play the `output.mp3` file.
5.  **Cleanup:** After playing the audio, the script removes the `output.mp3` file.

## Libraries Used

*   [**gTTS**](https://pypi.org/project/gTTS/): A Python library and CLI tool to interface with Google Text-to-Speech API.
*   [**pydub**](https://pypi.org/project/pydub/): A Python library to work with audio files. It's used here for playing the generated audio. `pydub` requires an audio playback library like `ffplay` or `simpleaudio` to be installed on your system.

## Setup and Usage

To run this project, follow these steps:

**1. Clone the repository:**

If you are working with this project locally, you can skip this step. If you are accessing it from a repository, you would typically clone it:

```bash
git clone <repository-url>
cd <repository-folder>
```

**2. Create a virtual environment (recommended):**

It's a good practice to create a virtual environment to manage project dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

*   **On Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
*   **On macOS and Linux:**
    ```bash
    source venv/bin/activate
    ```

**3. Install the dependencies:**

Install the required Python libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

**4. Install an audio playback library:**

`pydub` needs an audio playback library to play the audio. One of the easiest to install is `ffplay`. You can also use `simpleaudio`.

*   **To install `ffplay` (part of ffmpeg):**
    *   **Windows:** Download ffmpeg from the [official website](https://ffmpeg.org/download.html) and add the `bin` folder to your system's PATH.
    *   **macOS (using Homebrew):**
        ```bash
        brew install ffmpeg
        ```
    *   **Linux (using apt):**
        ```bash
        sudo apt-get install ffmpeg
        ```

**5. Run the script:**

Execute the `main.py` script to see the text-to-speech conversion in action.

```bash
python main.py
```

You should hear the audio playback of the text defined in the script.

## How to Contribute

This is a simple project, but you can contribute by:

*   Adding more examples with different languages.
*   Creating a more interactive script where the user can input the text.
*   Improving the documentation.

We hope this example is helpful for your learning journey!