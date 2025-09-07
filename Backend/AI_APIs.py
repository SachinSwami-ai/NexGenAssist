import os
from typing import Optional

# Try to load dotenv for local development, but don't fail if not available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not available, use environment variables directly

# For Streamlit Cloud, try to use st.secrets
try:
    import streamlit as st
    if hasattr(st, 'secrets'):
        # Use Streamlit secrets if available
        def get_env_var(key):
            return st.secrets.get(key, os.getenv(key))
    else:
        def get_env_var(key):
            return os.getenv(key)
except ImportError:
    def get_env_var(key):
        return os.getenv(key)

class AIModelHandler:
    def __init__(self):
        self.models = {
            "OpenAI": self._openai_response,
            "Gemini": self._gemini_response,
            "Groq": self._groq_response
        }
    
    def get_response(self, model_name: str, prompt: str) -> str:
        if model_name in self.models:
            return self.models[model_name](prompt)
        return f"Model {model_name} not supported"
    
    def _openai_response(self, prompt: str) -> str:
        try:
            import openai
            client = openai.OpenAI(api_key=get_env_var("OPENAI_API_KEY"))
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"OpenAI Error: {str(e)}"
    
    def _gemini_response(self, prompt: str) -> str:
        try:
            import google.generativeai as genai
            genai.configure(api_key=get_env_var("GEMINI_API_KEY"))
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Gemini Error: {str(e)}"
    
    def _groq_response(self, prompt: str) -> str:
        try:
            groq_api_key = get_env_var("GROQ_API_KEY")
            if not groq_api_key:
                return "Groq Error: GROQ_API_KEY not found in environment variables. Please add your Groq API key to the .env file."
            
            from groq import Groq
            client = Groq(api_key=groq_api_key)
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            return response.choices[0].message.content
        except Exception as e:
            if "invalid_api_key" in str(e):
                return "Groq Error: Invalid API key. Please check your GROQ_API_KEY in the .env file. Get a free API key from https://console.groq.com/"
            return f"Groq Error: {str(e)}"