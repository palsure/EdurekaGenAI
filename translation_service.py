"""
Translation services using Google Generative AI
"""
import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()


class TranslationService:
    def __init__(self):
        self.model = None
        self.is_configured = False
        
    def configure_api(self):
        """Configure Google Generative AI API"""
        api_key = os.getenv("GOOGLE_API_KEY")
        genai_model = os.getenv("GENAI_MODEL", "gemini-pro")
        
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        try:
            genai.configure(api_key=api_key)
            
            # Try to initialize the model
            try:
                self.model = genai.GenerativeModel(genai_model)
                # Test the model
                test_response = self.model.generate_content("Test")
                self.is_configured = True
                return f"Successfully configured with model: {genai_model}"
            except Exception as model_error:
                raise Exception(f"Could not configure GenAI model - {genai_model}. Please check the model name. Error: {model_error}")
            
        except Exception as e:
            raise Exception(f"Error configuring Google API Key: {e}")
    
    def translate_text(self, text, target_language):
        """Translate text to target language"""
        if not self.is_configured:
            raise Exception("Translation service not configured")
        
        try:
            prompt = f"Translate the following text to {target_language}, provide only the translated text:\n\n{text}"
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Error during translation: {e}")