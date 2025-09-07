import streamlit as st
import pandas as pd
from datetime import datetime
import sys
sys.path.append('../../Backend')
from AI_APIs import AIModelHandler

def show_chat_assist():
    st.subheader("💬 Chat Assist")
    
    # Initialize session state for chat
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "ai_handler" not in st.session_state:
        st.session_state.ai_handler = AIModelHandler()
    
    # Get selected model from sidebar
    selected_model = st.session_state.get('selected_model', 'OpenAI')
    st.info(f"Current model: {selected_model}")
    
    # Chat history controls
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Save Chat", disabled=not st.session_state.messages, use_container_width=True):
            df = pd.DataFrame(st.session_state.messages)
            df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            df['model'] = selected_model
            st.download_button(
                "📄 Download CSV",
                df.to_csv(index=False),
                f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                "text/csv",
                use_container_width=True
            )
    
    with col2:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    st.markdown("---")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input and response handling
    if prompt := st.chat_input("Ask me anything..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner(f"Getting response from {selected_model}..."):
                response = st.session_state.ai_handler.get_response(selected_model, prompt)
                st.markdown(response)
        
        # Add assistant message to history
        st.session_state.messages.append({"role": "assistant", "content": response})