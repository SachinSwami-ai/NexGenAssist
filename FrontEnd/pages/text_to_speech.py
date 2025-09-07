import streamlit as st
import sys
import os

# Add Backend to path
backend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'Backend')
if os.path.exists(backend_path):
    sys.path.insert(0, backend_path)

from text_to_speech import TextToSpeech

def show_text_to_speech():
    st.subheader("🔊 Text to Speech")
    
    # Check if OpenAI is selected for text to speech
    selected_model = st.session_state.get('selected_model', 'OpenAI')
    if selected_model != 'OpenAI':
        st.warning(f"⚠️ Text to Speech requires OpenAI's TTS. Currently: {selected_model}. Switch to OpenAI in sidebar.")
        st.info("Text to Speech is only available with OpenAI's TTS models.")
        return
    
    # Text input for speech conversion
    text_input = st.text_area("Enter text to convert to speech:")
    
    # Voice selection
    voice_option = st.selectbox(
        "Select Voice:",
        ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
    )
    
    # Convert to speech button
    if st.button("Convert to Speech"):
        if text_input.strip():
            with st.spinner("Converting text to speech..."):
                tts = TextToSpeech()
                audio_content = tts.convert_text_to_speech(text_input, voice_option)
                
                # Display audio result
                if isinstance(audio_content, bytes):
                    st.audio(audio_content, format="audio/mp3")
                    st.success("Audio generated successfully!")
                else:
                    st.error(audio_content)
        else:
            st.warning("Please enter some text to convert.")