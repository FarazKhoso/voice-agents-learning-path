from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

text = "Hello, this is a test."
tts = gTTS(text=text, lang='en')
output_file = "output.mp3"
tts.save(output_file)
print(f"Audio saved to {output_file}")





audio = AudioSegment.from_mp3(output_file)
play(audio)
os.remove(output_file)