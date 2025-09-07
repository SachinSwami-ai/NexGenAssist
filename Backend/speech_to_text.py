import os

# Try to load dotenv for local development, but don't fail if not available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

class SpeechToText:
    def __init__(self):
        pass
    
    def transcribe_audio(self, audio_file, model="google"):
        return self._transcribe_with_google(audio_file)
    
    def _transcribe_with_google(self, audio_file):
        try:
            import speech_recognition as sr
            
            # Use speech_recognition with audio file
            r = sr.Recognizer()
            
            # Convert audio to recognizable format
            with sr.AudioFile(audio_file) as source:
                audio_data = r.record(source)
            
            # Use Google's free speech recognition
            text = r.recognize_google(audio_data)
            return text
            
        except sr.UnknownValueError:
            return "Could not understand the audio. Please speak clearly and try again."
        except sr.RequestError as e:
            return f"Could not request results from speech recognition service: {e}"
        except Exception as e:
            return f"Speech recognition error: {str(e)}"