"""
Main Streamlit application for text translation
"""
import streamlit as st
from translation_service import TranslationService
from ui_components import (
    render_input_section, 
    render_language_selection, 
    render_translation_result, 
    render_audio_section
)

# Page config
st.set_page_config(page_title="Text Translator", layout="wide")

# Initialize session state
if 'translation_service' not in st.session_state:
    st.session_state.translation_service = TranslationService()

# Configure API (only once)
if not st.session_state.translation_service.is_configured:
    try:
        result = st.session_state.translation_service.configure_api()
        st.success(f"✅ {result}")
        st.rerun()
    except Exception as e:
        st.error(f"❌ {str(e)}")
        st.stop()

# Main App
st.title("🌐 Text Translator & Speech Converter")

# Layout with columns
col1, col2 = st.columns([1, 1])

with col1:
    # Render input section
    input_text = render_input_section()
    
    # Render language selection
    target_language, languages = render_language_selection()
    
    # Process button
    processing_button = st.button(
        "🔄 Start Processing", 
        use_container_width=False, 
        type="primary",
        disabled=(not input_text.strip())
    )

with col2:
    if processing_button and input_text.strip():
        with st.spinner(f"Translating input to {target_language} & generating audio..."):
            try:
                # Translate text
                translated_text = st.session_state.translation_service.translate_text(
                    input_text, target_language
                )
                
                # Render translation result
                render_translation_result(translated_text, target_language)
                
                # Render audio section
                language_code = languages[target_language]
                render_audio_section(translated_text, language_code, target_language)
                
            except Exception as e:
                st.error(f"❌ {str(e)}")
    
    elif not input_text.strip() and processing_button:
        st.warning("⚠️ Please enter text or upload a file to start process.")
    
    elif not input_text.strip():
        st.info("👈 Enter text or upload a file to get started!")

