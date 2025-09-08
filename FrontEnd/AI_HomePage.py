import streamlit as st
import os
import sys

# Add Backend to path for local development
backend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Backend')
if os.path.exists(backend_path):
    sys.path.insert(0, backend_path)

from pages.chat_assist import show_chat_assist
from pages.image_processor import show_image_processor
from pages.generate_image import show_generate_image
from pages.speech_to_text import show_speech_to_text
from pages.text_to_speech import show_text_to_speech

# Configure Streamlit page settings
st.set_page_config(
    page_title="NexGenAssist",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS styles
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%) !important;
    padding-top: 80px;
}

.stApp {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%) !important;
}

section[data-testid="stMain"] {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%) !important;
}

.fixed-header {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100vw !important;
    z-index: 999999 !important;
    background: linear-gradient(90deg, #ff6b6b, #ffa726) !important;
    padding: 15px !important;
    text-align: center !important;
    color: white !important;
    font-size: 24px !important;
    font-weight: bold !important;
    margin: 0 !important;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3) !important;
}

.stApp {
    padding-top: 0 !important;
}

.stApp > div:first-child {
    padding-top: 0 !important;
}

.clear-chat-fixed {
    position: fixed !important;
    bottom: 20px !important;
    left: 20px !important;
    z-index: 1000 !important;
    background: #e74c3c !important;
    color: white !important;
    border: none !important;
    padding: 12px 20px !important;
    border-radius: 25px !important;
    font-weight: bold !important;
    cursor: pointer !important;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
    font-size: 14px !important;
}

.clear-chat-fixed:hover {
    background: #c0392b !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 12px rgba(0,0,0,0.3) !important;
}

.selected-button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
    border: 2px solid #667eea !important;
    transform: translateY(-2px) !important;
}

.selected-button:hover {
    background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%) !important;
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
}

/* Sidebar styling for all versions */
.stSidebar,
.stSidebar > div,
.stSidebarContent,
.css-1d391kg,
.css-17lntkn,
.css-pkbazv,
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div,
section[data-testid="stSidebar"] .stSidebarContent,
.st-emotion-cache-1cypcdb,
.st-emotion-cache-6qob1r {
    background: linear-gradient(180deg, #ff9a9e 0%, #fecfef 100%) !important;
}

/* Main content styling */
.main,
.stApp,
.stMainBlockContainer,
section[data-testid="stMain"],
.st-emotion-cache-z5fcl4,
.st-emotion-cache-18ni7ap {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%) !important;
}

.chat-message {
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    background: rgba(255, 255, 255, 0.8);
}

.clear-chat-btn {
    background: #ff4757;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 20px;
    cursor: pointer;
    font-weight: bold;
    margin: 10px 0;
}

.clear-chat-btn:hover {
    background: #ff3742;
}

.processing-icon {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 3px solid #f3f3f3;
    border-top: 3px solid #ff6b6b;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-right: 10px;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #ff6b6b;
    color: white;
    text-align: center;
    padding: 10px;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# Hide default Streamlit navigation elements and style chat input
st.markdown("""
<style>
    .css-1d391kg, .css-17lntkn, .css-pkbazv, [data-testid="stSidebarNav"], 
    .css-1544g2n, .css-1y4p8pa { display: none !important; }
    
    /* Style chat input with warm theme */
    .stChatInput {
        background: linear-gradient(135deg, #ff9a56 0%, #ff6b35 100%) !important;
        border-radius: 30px !important;
        padding: 5px !important;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3) !important;
    }
    
    .stChatInput > div {
        background: transparent !important;
    }
    
    .stChatInput > div > div {
        background: transparent !important;
    }
    
    .stChatInput > div > div > div {
        background: transparent !important;
    }
    
    .stChatInput input {
        background: rgba(255, 255, 255, 0.95) !important;
        color: #d63031 !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 20px !important;
    }
    
    .stChatInput input::placeholder {
        color: #ff6b35 !important;
        font-weight: 500 !important;
        opacity: 0.8 !important;
    }
    
    .stChatInput input:focus {
        box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.3) !important;
        outline: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Application header with logo
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 10px;">
    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 5px;">
        <svg width="30" height="30" viewBox="0 0 60 60" style="margin-right: 8px;">
            <defs>
                <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#00d4ff;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#5b73e8;stop-opacity:1" />
                </linearGradient>
            </defs>
            <circle cx="30" cy="30" r="28" fill="url(#logoGrad)" stroke="white" stroke-width="2"/>
            <path d="M20 25 L25 20 L35 20 L40 25 L40 35 L35 40 L25 40 L20 35 Z" fill="white" opacity="0.9"/>
            <circle cx="26" cy="28" r="2" fill="#667eea"/>
            <circle cx="34" cy="28" r="2" fill="#667eea"/>
            <path d="M24 34 Q30 38 36 34" stroke="#667eea" stroke-width="2" fill="none" stroke-linecap="round"/>
            <path d="M15 15 L20 10 M45 15 L40 10 M15 45 L20 50 M45 45 L40 50" stroke="white" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <h1 style="margin: 0; font-size: 1.25em;">NexGenAssist</h1>
    </div>
    <p style="margin: 0; font-size: 0.6em;">Your AI-powered assistant for multiple tasks</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state variables
if "selected_feature" not in st.session_state:
    st.session_state.selected_feature = "Chat Assist"
if "selected_model" not in st.session_state:
    st.session_state.selected_model = "OpenAI"

# Sidebar navigation and controls
with st.sidebar:
    # Sidebar logo
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <svg width="40" height="40" viewBox="0 0 60 60">
            <defs>
                <linearGradient id="sidebarLogoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#00d4ff;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#5b73e8;stop-opacity:1" />
                </linearGradient>
            </defs>
            <circle cx="30" cy="30" r="28" fill="url(#sidebarLogoGrad)" stroke="#667eea" stroke-width="2"/>
            <path d="M20 25 L25 20 L35 20 L40 25 L40 35 L35 40 L25 40 L20 35 Z" fill="white" opacity="0.9"/>
            <circle cx="26" cy="28" r="2" fill="#667eea"/>
            <circle cx="34" cy="28" r="2" fill="#667eea"/>
            <path d="M24 34 Q30 38 36 34" stroke="#667eea" stroke-width="2" fill="none" stroke-linecap="round"/>
            <path d="M15 15 L20 10 M45 15 L40 10 M15 45 L20 50 M45 45 L40 50" stroke="#667eea" stroke-width="2" stroke-linecap="round"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    st.header("🚀 Features")
    
    # Feature selection buttons
    features = [
        ("💬 Chat Assist", "Chat Assist"),
        ("🖼️ Image Processor", "Image Processor"),
        ("🎨 Generate Image", "Generate Image"),
        ("🎤 Speech to Text", "Speech to Text"),
        ("🔊 Text to Speech", "Text to Speech")
    ]
    
    # Render feature buttons with selection highlighting
    for label, feature in features:
        if st.session_state.selected_feature == feature:
            st.markdown(f'<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 8px; border-radius: 5px; text-align: center; margin-bottom: 5px;">{label}</div>', unsafe_allow_html=True)
        else:
            if st.button(label, use_container_width=True, key=f"feat_{feature}"):
                st.session_state.selected_feature = feature
                st.rerun()
    
    st.markdown("---")
    st.header("Model Selection")
    
    # AI model selection buttons with feature compatibility
    models = [("🤖 OpenAI", "OpenAI"), ("💎 Gemini", "Gemini"), ("⚡ Groq", "Groq")]
    
    # Define which features require OpenAI
    openai_only_features = ["Image Processor", "Generate Image", "Speech to Text", "Text to Speech"]
    selected_feature = st.session_state.selected_feature
    
    # Render model buttons with selection highlighting and disable logic
    for label, model in models:
        is_selected = st.session_state.selected_model == model
        is_disabled = model != "OpenAI" and selected_feature in openai_only_features
        
        if is_selected:
            st.markdown(f'<div style="background: linear-gradient(135deg, #ff6b6b 0%, #ffa726 100%); color: white; padding: 8px; border-radius: 5px; text-align: center; margin-bottom: 5px;">{label}</div>', unsafe_allow_html=True)
        elif is_disabled:
            st.markdown(f'<div style="background: #cccccc; color: #666666; padding: 8px; border-radius: 5px; text-align: center; margin-bottom: 5px; opacity: 0.5;">{label} (Not Available)</div>', unsafe_allow_html=True)
        else:
            if st.button(label, use_container_width=True, key=f"model_{model}"):
                st.session_state.selected_model = model
                st.rerun()
    
    # Show compatibility info
    if selected_feature in openai_only_features:
        st.info(f"ℹ️ {selected_feature} requires OpenAI model")

# Route to selected feature page
feature_map = {
    "Chat Assist": show_chat_assist,
    "Image Processor": show_image_processor,
    "Generate Image": show_generate_image,
    "Speech to Text": show_speech_to_text,
    "Text to Speech": show_text_to_speech
}

feature_map[st.session_state.selected_feature]()

# Fixed footer at bottom
st.markdown("""
<div style="position: fixed; bottom: 0; left: 0; right: 0; background: #f0f2f6; padding: 10px; text-align: center; border-top: 1px solid #e0e0e0; z-index: 1000;">
    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 5px;">
        <svg width="20" height="20" viewBox="0 0 60 60" style="margin-right: 8px;">
            <defs>
                <linearGradient id="footerLogoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#00d4ff;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#5b73e8;stop-opacity:1" />
                </linearGradient>
            </defs>
            <circle cx="30" cy="30" r="28" fill="url(#footerLogoGrad)"/>
            <path d="M20 25 L25 20 L35 20 L40 25 L40 35 L35 40 L25 40 L20 35 Z" fill="white" opacity="0.9"/>
            <circle cx="26" cy="28" r="2" fill="#667eea"/>
            <circle cx="34" cy="28" r="2" fill="#667eea"/>
            <path d="M24 34 Q30 38 36 34" stroke="#667eea" stroke-width="2" fill="none" stroke-linecap="round"/>
        </svg>
        <span style="color: #666; font-size: 0.8em; font-weight: bold;">NexGenAssist</span>
    </div>
    <p style="margin: 0; color: #666; font-size: 0.7em;">
        © 2024 All rights reserved. | 
        <a href="https://github.com" style="color: #667eea; text-decoration: none;">GitHub</a> | 
        <a href="#" style="color: #667eea; text-decoration: none;">Documentation</a>
    </p>
</div>
<div style="height: 60px;"></div>
""", unsafe_allow_html=True)