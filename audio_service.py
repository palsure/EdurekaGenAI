"""
Text-to-speech services using gTTS
"""
import tempfile
import os
from gtts import gTTS
from gtts.lang import tts_langs
import streamlit as st


class AudioService:
    @staticmethod
    def get_supported_languages():
        """Get list of supported languages for TTS"""
        try:
            return tts_langs()
        except Exception:
            return {}
    
    @staticmethod
    def text_to_speech(text, language_code):
        """Convert text to speech and return audio file path"""
        try:
            # Check if language is supported by gTTS
            supported_langs = AudioService.get_supported_languages()
            
            if language_code not in supported_langs:
                raise Exception(f"Language code '{language_code}' not supported by gTTS")
                
            tts = gTTS(text=text, lang=language_code)
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp_file.name)
            return temp_file.name
            
        except Exception as e:
            raise Exception(f"Error during text-to-speech conversion: {e}")
    
    @staticmethod
    def cleanup_audio_file(file_path):
        """Clean up temporary audio file"""
        try:
            if file_path and os.path.exists(file_path):
                os.remove(file_path)
        except Exception:
            pass  # Ignore cleanup errors