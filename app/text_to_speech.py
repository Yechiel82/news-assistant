from pathlib import Path
from openai import OpenAI

import sys

def text_to_speech(text):
    client = OpenAI()
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(speech_file_path)
    return speech_file_path

# CLI usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python text_to_speech.py 'text to convert to speech'")
        sys.exit(1)
    text = sys.argv[1]
    speech_file = text_to_speech(text)
    print(f"Speech file created at: {speech_file}")

