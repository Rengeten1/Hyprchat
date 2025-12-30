from ollama import chat
from listen_client import Listener 
from speak_client import Speaker
import re

class ChatClient:
    def __init__(self, model='gemma3:4b'):
        self.model = model
        self.messages = [{'role':'system', 'content': 'You are a voice assistant. Your goal is to be exact and brief. Answer in short precice method.'}]
        self.listen_client = Listener()
        self.speak_client = Speaker()

    def ask(self, user_input):
    
        self.messages.append({'role': 'user', 'content': user_input})
    
        stream = chat(
            model=self.model,
            messages=self.messages,
            stream=True,)
        
        # stream output of the response
        full_response = ""
        sentence_buffer = ""

        for chunk in stream:
            content = chunk.message.content
            print(content, end='', flush=True)
            full_response += content
            sentence_buffer += content
            
            # audio output of the text speaks on each of the puncts
            if any(punct in content for punct in ['.', '?', '!', '\n']):
                tts = sentence_buffer.strip()
                if tts:
                    self.speak_client.speak(tts)
                sentence_buffer = ""
        
        if sentence_buffer.strip():
            self.speak_client.speak(sentence_buffer.strip())
        
        print()
        # updating history
        self.messages.append({'role': 'assistant', 'content': full_response})

    def run(self):
        while True:
            try:
                user_input = self.listen_client.hear()
                
                if user_input is None:
                    continue
                else:
                    self.ask(user_input)
            except Exception as e:
                print(f"An error occured: {e}")
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    print("Welcome to Hyprchat")
    print("---------------------")
    print("Please say something!")
    client = ChatClient()
    client.run()
