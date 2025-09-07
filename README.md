# NexGenAssist 🤖

Your AI-powered assistant for multiple tasks including chat, image processing, image generation, speech-to-text, and text-to-speech.

## Features

- **💬 Chat Assist**: Interactive chat with OpenAI, Gemini, and Groq models
- **🖼️ Image Processor**: AI-powered image analysis and description using OpenAI Vision
- **🎨 Generate Image**: Create images from text descriptions using DALL-E
- **🎤 Speech to Text**: Convert audio recordings to text using OpenAI Whisper
- **🔊 Text to Speech**: Convert text to natural speech using OpenAI TTS

## Prerequisites

### System Requirements
- Python 3.8 or higher
- Internet connection for API calls
- Microphone access (for Speech to Text feature)

### API Keys Required
You'll need API keys from the following services:

1. **OpenAI API Key** (Required for most features)
   - Sign up at: https://platform.openai.com/
   - Get API key from: https://platform.openai.com/api-keys
   - Used for: Chat, Image Analysis, Image Generation, Speech to Text, Text to Speech

2. **Google Gemini API Key** (Optional - for Gemini chat model)
   - Sign up at: https://makersuite.google.com/
   - Get API key from: https://makersuite.google.com/app/apikey
   - Used for: Chat only

3. **Groq API Key** (Optional - for Groq chat model)
   - Sign up at: https://console.groq.com/
   - Get API key from: https://console.groq.com/keys
   - Used for: Chat only

## Installation Steps

### 1. Clone the Repository
```bash
git clone <repository-url>
cd NexGenAssist
```

### 2. Install Python Dependencies
```bash
pip install -r Backend/requirements.txt
```

### 3. Install Streamlit
```bash
pip install streamlit
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory:
```bash
# Required for most features
OPENAI_API_KEY=your_openai_api_key_here

# Optional - for additional chat models
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Install Audio Dependencies (Optional)
For Speech to Text feature:
```bash
pip install audio-recorder-streamlit
```

## Running the Application

### 1. Navigate to Frontend Directory
```bash
cd FrontEnd
```

### 2. Start the Streamlit Application
```bash
streamlit run AI_HomePage.py
```

### 3. Access the Application
- The app will automatically open in your default browser
- If not, go to: http://localhost:8501

## Usage Guide

### Feature Availability by Model

| Feature | OpenAI | Gemini | Groq |
|---------|--------|--------|------|
| Chat Assist | ✅ | ✅ | ✅ |
| Image Processor | ✅ | ❌ | ❌ |
| Generate Image | ✅ | ❌ | ❌ |
| Speech to Text | ✅ | ❌ | ❌ |
| Text to Speech | ✅ | ❌ | ❌ |

### How to Use Each Feature

1. **Select Model**: Choose your preferred AI model from the sidebar
2. **Select Feature**: Click on the desired feature from the sidebar
3. **Follow Instructions**: Each feature has specific instructions on the main page

### Chat Assist
- Type your questions in the chat input
- Save chat history as CSV
- Clear chat when needed

### Image Processor
- Upload an image (JPG, JPEG, PNG)
- Ask questions about the image in the chat
- Requires OpenAI model selection

### Generate Image
- Describe the image you want to create
- Select image size
- Requires OpenAI model selection

### Speech to Text
- Click to record audio
- Get transcription of your speech
- Requires OpenAI model selection

### Text to Speech
- Enter text to convert
- Select voice option
- Requires OpenAI model selection

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure API keys are correctly set in `.env` file
   - Check if API keys have sufficient credits/quota

2. **Module Not Found Errors**
   - Run: `pip install -r Backend/requirements.txt`
   - Ensure you're in the correct directory

3. **Audio Recording Issues**
   - Allow microphone access in your browser
   - Install: `pip install audio-recorder-streamlit`

4. **Image Analysis Not Working**
   - Ensure OpenAI is selected as the model
   - Check OpenAI API key and credits

### Error Messages

- **"Feature requires OpenAI"**: Switch to OpenAI model in sidebar
- **"API Connection Error"**: Check internet connection and API keys
- **"Invalid API Key"**: Verify API key in `.env` file

## File Structure

```
NexGenAssist/
├── Backend/
│   ├── AI_APIs.py              # AI model handlers
│   ├── image_processor.py      # Image analysis logic
│   ├── image_generator.py      # Image generation logic
│   ├── speech_to_text.py       # Speech recognition logic
│   ├── text_to_speech.py       # Text to speech logic
│   └── requirements.txt        # Python dependencies
├── FrontEnd/
│   ├── AI_HomePage.py          # Main application file
│   ├── CSS Design/
│   │   └── styles.css          # Custom styling
│   └── pages/
│       ├── chat_assist.py      # Chat interface
│       ├── image_processor.py  # Image analysis interface
│       ├── generate_image.py   # Image generation interface
│       ├── speech_to_text.py   # Speech recognition interface
│       └── text_to_speech.py   # Text to speech interface
├── .env                        # Environment variables (create this)
└── README.md                   # This file
```

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Ensure all prerequisites are met
3. Verify API keys and internet connection

## License

This software is provided "as is" without warranty of any kind.