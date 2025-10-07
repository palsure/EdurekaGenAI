"""
UI components for the translation app
"""
import streamlit as st
from file_processors import process_uploaded_file


def render_input_section():
    """Render the input section of the app"""
    # Input method selection
    input_method = st.radio( 
        "Select input option:",
        ["✍️ Type Text", "📁 Upload File"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    input_text = ""
    
    if input_method == "✍️ Type Text":
        input_text = st.text_area(
            "Enter text to translate:", 
            height=200,
            key="input_text"
        )
    
    elif input_method == "📁 Upload File":
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['txt', 'pdf', 'docx', "csv", "xlsx", "xls"],
            help="Supported formats: TXT, PDF, DOCX, CSV, XLSX, XLS"
        )
        
        if uploaded_file is not None:
            st.info(f"📄 File uploaded: {uploaded_file.name}")
            
            with st.spinner("Extracting text from file..."):
                extracted_text = process_uploaded_file(uploaded_file)
                
            if not extracted_text.startswith("Error"):
                input_text = extracted_text
                
                # Show preview of extracted text
                st.text_area(
                    "Extracted text preview:",
                    value=extracted_text[:500] + ("..." if len(extracted_text) > 500 else ""),
                    height=150,
                    disabled=True
                )
                
                if len(extracted_text) > 500:
                    st.info(f"📊 Total characters extracted: {len(extracted_text)}")
            else:
                st.error(extracted_text)
    
    return input_text


def render_language_selection():
    """Render language selection dropdown"""
    languages = {
        "English": "en",
        "Spanish": "es", 
        "French": "fr",
        "German": "de",
        "Chinese": "zh",
        "Hindi": "hi",
        "Japanese": "ja",
        "Russian": "ru",
        "Italian": "it",
        "Portuguese": "pt",
        "Arabic": "ar",
        "Korean": "ko",
        "Dutch": "nl",
        "Swedish": "sv",
        "Turkish": "tr",
        "Vietnamese": "vi",
        "Tamil": "ta",
        "Malayalam": "ml",
        "Telugu": "te",
        "Kannada": "kn"
    }
    
    target_language = st.selectbox("Select target language:", list(languages.keys()))
    return target_language, languages


def render_translation_result(translated_text, target_language):
    """Render the translation result section"""
    st.subheader("📄 Translation")
    st.success("✅ Translation successful!")
    
    # Display translated text
    st.text_area(
        "Translated text:", 
        value=translated_text, 
        height=200,
        key="output_text"
    )
    
    # Download translated text button
    st.download_button(
        "📥 Download Translation",
        data=translated_text,
        file_name=f"translation_{target_language.lower()}.txt",
        mime="text/plain"
    )


def render_audio_section(translated_text, language_code, target_language):
    """Render the audio conversion section"""
    from audio_service import AudioService
    
    st.subheader("🔊 Text-to-Speech")
    
    # Warning for very long text
    if len(translated_text) > 5000:
        st.warning("⚠️ Text is very long. Audio generation might take time or fail.")
    
    with st.spinner("Converting to speech..."):
        try:
            # For very long text, truncate for TTS
            tts_text = translated_text[:5000] if len(translated_text) > 5000 else translated_text
            
            audio_file = AudioService.text_to_speech(tts_text, language_code)
            
            st.success("✅ Audio generated successfully!")
            
            if len(translated_text) > 5000:
                st.info("🔊 Audio generated for first 5000 characters only.")
            
            # Play audio
            with open(audio_file, "rb") as file:
                audio_bytes = file.read()
                st.audio(audio_bytes, format="audio/mp3")
                
                # Download button
                st.download_button(
                    "⬇️ Download Audio",
                    data=audio_bytes,
                    file_name=f"translated_audio_{target_language.lower()}.mp3",
                    mime="audio/mp3"
                )
            
            # Clean up
            AudioService.cleanup_audio_file(audio_file)
            
        except Exception as e:
            st.error(str(e))