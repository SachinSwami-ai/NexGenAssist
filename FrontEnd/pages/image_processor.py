import streamlit as st
import sys
sys.path.append('../../Backend')
from image_processor import ImageProcessor

def show_image_processor():
    st.subheader("🖼️ Image Processor")
    
    # Display model requirement message
    selected_model = st.session_state.get('selected_model', 'OpenAI')
    if selected_model != 'OpenAI':
        st.warning(f"⚠️ Image analysis requires OpenAI model. Currently selected: {selected_model}")
        st.info("Please switch to OpenAI in the sidebar to use image analysis features.")
    else:
        st.success("✅ OpenAI selected - Image analysis available")
    
    # Image upload
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", width=400)
        
        # Check if OpenAI is selected for image analysis
        selected_model = st.session_state.get('selected_model', 'OpenAI')
        if selected_model != 'OpenAI':
            st.warning(f"⚠️ Image analysis requires OpenAI. Currently: {selected_model}. Switch to OpenAI in sidebar.")
            return
        
        st.info("💬 Ask questions about your image below")
        
        # Initialize image chat history
        if "image_messages" not in st.session_state:
            st.session_state.image_messages = []
        
        # Display chat history
        for message in st.session_state.image_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Image chat input
        if prompt := st.chat_input("Ask about this image..."):
            # Add user message
            st.session_state.image_messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate AI response about image
            with st.chat_message("assistant"):
                with st.spinner("Analyzing image..."):
                    try:
                        processor = ImageProcessor()
                        custom_prompt = f"User question: {prompt}. Please analyze the image and answer this specific question."
                        result = processor._get_ai_description_with_prompt(uploaded_file, custom_prompt)
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"API Connection Error: {str(e)}")
                        result = f"Failed to connect to OpenAI API: {str(e)}"
            
                        # Add response to history
                        st.session_state.image_messages.append({"role": "assistant", "content": result})
                    except Exception as e:
                        error_msg = f"Failed to connect to OpenAI API: {str(e)}"
                        st.session_state.image_messages.append({"role": "assistant", "content": error_msg})
        
        # Clear chat history
        if st.button("🗑️ Clear Chat"):
            st.session_state.image_messages = []
            st.rerun()