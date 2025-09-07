import os

# Try to load dotenv for local development, but don't fail if not available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# For Streamlit Cloud, try to use st.secrets
try:
    import streamlit as st
    if hasattr(st, 'secrets'):
        def get_env_var(key):
            return st.secrets.get(key, os.getenv(key))
    else:
        def get_env_var(key):
            return os.getenv(key)
except ImportError:
    def get_env_var(key):
        return os.getenv(key)

class ImageGenerator:
    def __init__(self):
        pass
    
    def generate_image(self, prompt, size="1024x1024"):
        return self._generate_with_dalle(prompt, size)
    
    def _generate_with_dalle(self, prompt, size="1024x1024"):
        try:
            import openai
            client = openai.OpenAI(api_key=get_env_var("OPENAI_API_KEY"))
            
            # Try DALL-E 3 first
            try:
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size=size,
                    quality="standard",
                    n=1,
                )
                return response.data[0].url
            except Exception as dalle3_error:
                if "model_not_found" in str(dalle3_error) or "403" in str(dalle3_error):
                    # Fallback to DALL-E 2
                    response = client.images.generate(
                        model="dall-e-2",
                        prompt=prompt,
                        size="1024x1024",  # DALL-E 2 supports limited sizes
                        n=1,
                    )
                    return response.data[0].url
                else:
                    raise dalle3_error
                    
        except Exception as e:
            return f"DALL-E Error: {str(e)}"
    
