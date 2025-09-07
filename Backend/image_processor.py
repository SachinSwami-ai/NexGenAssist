import os
from PIL import Image
import io

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

class ImageProcessor:
    def __init__(self):
        pass
    
    def analyze_image(self, image_file):
        try:
            # Open image
            image = Image.open(image_file)
            return self._analyze_image(image)
        except Exception as e:
            return f"Image analysis error: {str(e)}"
    
    def _analyze_image(self, image):
        # Use OpenAI API for image analysis - no fallback
        return self._get_ai_description(image)
    
    def _get_ai_description(self, image):
        import openai
        import base64
        import io
        
        client = openai.OpenAI(api_key=get_env_var("OPENAI_API_KEY"))
        
        # Convert image to base64
        img_buffer = io.BytesIO()
        image.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Please provide a detailed description of this image, including objects, people, colors, setting, mood, and any notable details."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{img_base64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=300
        )
        
        return response.choices[0].message.content
    
    def _get_ai_description_with_prompt(self, image_file, custom_prompt):
        import openai
        import base64
        import io
        from PIL import Image
        
        client = openai.OpenAI(api_key=get_env_var("OPENAI_API_KEY"))
        
        # Open and convert image to base64
        image = Image.open(image_file)
        img_buffer = io.BytesIO()
        image.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": custom_prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{img_base64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=300
        )
        
        return response.choices[0].message.content
    
