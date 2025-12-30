# Hyprchat

Hyprchat is a voice assistant that allows you to have conversation with local LLM via Ollama. The project combines Speech-to-text (STT), a local LLM backend and Text-to-Speech (TTS) to deliver a conversation assistant.

## Features
- Local & Private, all the data is stored on the machine itself.
- Supports different LLM's such as Llama3, Mistral Phi-4 etc.
- Detects voice activity and stops recording when you finish speaking.
- Optimized for low latency.
- Custom Personas, easily change personality of the assistant.

## Installation

First clone the repository:

```
git clone https://github.com/Rengeten1/Hyprchat.git
```

Then install the packages:

```
python -m venv .venv
source .venv/bin/activate # for linux
pip install -r requirements.txt
```

Download for voice assistant:

```
# The Model (approx 330MB)
wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx -O kokoro-v0_19.onnx

# The Voices (approx 30MB)
wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
```


## Usage

To run the application:

```
python chat.py
```

Then speak and talk to the voice assistant!


