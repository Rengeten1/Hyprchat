import re
import sounddevice as sd
from kokoro_onnx import Kokoro

class Speaker:

    def __init__(self, model_path="kokoro-v0_19.onnx", voices_path="voices-v1.0.bin"):
        # initialize the engine
        self.kokoro = Kokoro(model_path, voices_path)
        self.voice = "am_adam"
        self.speed = 1.0
        self.language = "en-us"

    def _clean_text(self, text):

        # removing markdown bold and italic syntax
        text = re.sub(r'\*\*|__', '', text)

        # removing emojis and symbols
        text = re.sub(r'[^a-zA-Z0-9\s\.\,\!\?\'\"]', '', text)

        return text 

    def speak(self, user_intent):
        clean_text = self._clean_text(user_intent)
        
        if not clean_text:
            return

        # Generate audio 
        samples, sample_rate = self.kokoro.create(
            clean_text,
            voice=self.voice,
            speed=self.speed,
            lang=self.language
        )

        # play the audio
        sd.play(samples, sample_rate)
        sd.wait() # ensures it finished before next sentence start

if __name__ == "__main__":
    speaker_client = Speaker()
    input = input("Type something: ")
    speaker_client.speak(input)
