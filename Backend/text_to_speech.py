import os
from dotenv import load_dotenv

load_dotenv()

class TextToSpeech:
    def __init__(self):
        pass
    
    def convert_text_to_speech(self, text, voice="alloy", model="tts-1"):
        try:
            if model == "tts-1":
                return self._convert_with_openai(text, voice)
            else:
                return "Model not supported"
                
        except Exception as e:
            return f"Text to speech error: {str(e)}"
    
    def _convert_with_openai(self, text, voice):
        try:
            import openai
            client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            
            response = client.audio.speech.create(
                model="tts-1",
                voice=voice,
                input=text
            )
            
            return response.content
        except Exception as e:
            return f"OpenAI TTS Error: {str(e)}"