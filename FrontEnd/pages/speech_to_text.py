import streamlit as st
import sys
import io
import os

# Add Backend to path
backend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'Backend')
if os.path.exists(backend_path):
    sys.path.insert(0, backend_path)

from speech_to_text import SpeechToText

def show_speech_to_text():
    st.subheader("🎤 Speech to Text")
    
    # Check if OpenAI is selected for speech recognition
    selected_model = st.session_state.get('selected_model', 'OpenAI')
    if selected_model != 'OpenAI':
        st.warning(f"⚠️ Speech to Text requires OpenAI's Whisper. Currently: {selected_model}. Switch to OpenAI in sidebar.")
        st.info("Speech to Text is only available with OpenAI's Whisper model.")
        return
    
    # Audio recording section
    try:
        from audio_recorder_streamlit import audio_recorder
        
        st.info("🎤 Record your voice and get transcription")
        
        # Audio recorder widget
        audio_bytes = audio_recorder(
            text="Click to record",
            recording_color="#e8b62c",
            neutral_color="#6aa36f",
            icon_name="microphone",
            icon_size="2x"
        )
        
        # Process recorded audio
        if audio_bytes:
            st.audio(audio_bytes, format="audio/wav")
            st.success("Audio recorded successfully!")
            
            # Transcription button
            if st.button("Get Transcription", use_container_width=True):
                with st.spinner("Transcribing audio..."):
                    stt = SpeechToText()
                    audio_file = io.BytesIO(audio_bytes)
                    audio_file.name = "recording.wav"
                    result = stt.transcribe_audio(audio_file)
                    
                    # Display transcription result
                    if "Error" not in result and "unavailable" not in result:
                        st.success("Transcription completed!")
                        st.text_area("Transcribed Text:", result, height=100)
                        st.code(result)
                    else:
                        st.warning("Transcription service unavailable.")
                        st.info("Please use manual text input below.")
    
    except ImportError:
        st.error("Audio recorder not available. Please install: pip install audio-recorder-streamlit")
    
    # Manual text input section
    st.markdown("---")
    st.info("📝 Manual text input:")
    manual_text = st.text_area("Type or paste your text here:", height=100)
    
    if manual_text:
        st.success("Text ready for processing!")
        if st.button("Process Text"):
            st.text_area("Processed Text:", manual_text, height=100)