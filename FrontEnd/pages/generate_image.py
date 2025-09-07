import streamlit as st
import sys
sys.path.append('../../Backend')
from image_generator import ImageGenerator

def show_generate_image():
    st.subheader("🎨 Generate Image")
    
    # Check if OpenAI is selected for image generation
    selected_model = st.session_state.get('selected_model', 'OpenAI')
    if selected_model != 'OpenAI':
        st.warning(f"⚠️ Image generation requires OpenAI's DALL-E. Currently: {selected_model}. Switch to OpenAI in sidebar.")
        st.info("Image generation is only available with OpenAI's DALL-E models.")
        return
    
    # Image generation form
    image_prompt = st.text_area(
        "Describe the image you want to generate:", 
        height=100, 
        placeholder="e.g., A beautiful sunset over mountains with a lake in the foreground"
    )
    
    # Image size selection
    image_size = st.selectbox("Size:", ["1024x1024", "1792x1024", "1024x1792"])
    st.info("Will fallback to DALL-E 2 if DALL-E 3 is not accessible")
    
    # Generate image button
    if st.button("Generate Image", use_container_width=True):
        if image_prompt.strip():
            with st.spinner("Generating image with DALL-E..."):
                img_gen = ImageGenerator()
                result = img_gen.generate_image(image_prompt, image_size)
                
                # Display result
                if result.startswith("http"):
                    st.success("Image generated successfully!")
                    st.image(result, caption=f"Generated: {image_prompt[:50]}...")
                    st.markdown(f"[Download Image]({result})")
                elif "Error" in result:
                    st.error(result)
                else:
                    st.info(result)
        else:
            st.warning("Please enter a description for the image you want to generate.")