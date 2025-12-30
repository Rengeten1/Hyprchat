import os
import sys
import ctypes
import speech_recognition as sr

# silencing the ALSA logs
ERROR_HANDLER_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p)
def py_error_handler(filename, line, function, err, fmt):
    pass
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

try:
    asound = ctypes.cdll.LoadLibrary('libasound.so.2')
    asound.snd_lib_error_set_handler(c_error_handler)
except:
    pass # Fallback for non-Linux systemsclass VoiceClient: 

class Listener:
    def __init__(self, language='english'):
        self.recognizer = sr.Recognizer()
        self.language = language
        self.duration = 0.5 # 1.0 for loud areas 

    def hear(self):
        try: 
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=self.duration)
                audio = self.recognizer.listen(source)
                
        except Exception as e:
            print(f"An Error occured: {e}")

        try:
            # adjusting for ambient noise
            output = self.recognizer.recognize_whisper(audio, language=self.language)
            print("You:", output)
            return output
        except sr.UnknownValueError:
            print("Whisper could not understand audio")

if __name__ == "__main__":
    client = VoiceClient()
    client.hear()
