# Import the necessary libraries
import speech_recognition as sr
import time

def listen_and_recognize():
    """
    This function listens for audio from the microphone, recognizes the speech using Google's Web Speech API, and returns the recognized text.
    """
    # Create a Recognizer instance
    r = sr.Recognizer()
    # Create a Microphone instance
    mic = sr.Microphone()

    # Adjust for ambient noise before listening
    with mic as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source)
        print("Listening...")

    # Listen for audio from the microphone
    with mic as source:
        # Listen for up to 10 seconds, and stop listening if there's a pause of 10 seconds
        audio = r.listen(source, timeout=10, phrase_time_limit=10)

    try:
        # Recognize speech using Google's Web Speech API
        print("Recognizing speech...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text

    except sr.UnknownValueError:
        # Handle cases where the speech is unintelligible
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        # Handle cases where there's a network error
        print(f"Network error; check your internet connection: {e}")

if __name__ == "__main__":
    # Main loop to continuously listen and recognize speech
    while True:
        try:
            # Call the function to listen and recognize speech
            listen_and_recognize()
            print("-" * 50)
        except KeyboardInterrupt:
            # Handle Ctrl+C to exit the program gracefully
            print("\nBye!")
            break