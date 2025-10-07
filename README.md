# 🌐 Text Translator & Speech Converter

A powerful Streamlit-based application that translates text using Google's Generative AI and converts translations to speech using Google Text-to-Speech (gTTS).

## ✨ Features

- **Multi-format Input Support**: Type text or upload files (TXT, PDF, DOCX, CSV, XLSX, XLS)
- **AI-Powered Translation**: Uses Google's Gemini AI models for accurate translations
- **Text-to-Speech**: Convert translations to audio with download capability
- **Multi Languages**: Support for major world languages including English, Spanish, French, German, Chinese, Hindi, Arabic, and more
- **File Processing**: Extract and translate text from various document formats
- **Modular Architecture**: Clean, maintainable code structure
- **Error Handling**: Robust error handling with user-friendly messages

## 🚀 Quick Start

### 1. Clone or Download
```bash
git clone <repository-url>
cd project
```

### 2. Install Dependencies
```bash
# Create virtual environment (recommended)
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a `.env` file in the project root:
```env
# Google Generative AI API Key
GOOGLE_API_KEY=your_google_api_key_here

# Google Generative AI Model (optional)
GENAI_MODEL=gemini-2.0-flash
```

### 4. Get Google API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the generated key
4. Paste it in your `.env` file

### 5. Run the Application
```bash
streamlit run translate/translate_app.py
```

## 📁 Project Structure

```
project/
├── .env                    # Environment variables (keep secret!)
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── myenv/                 # Virtual environment
└── translate/             # Main application package
    ├── __init__.py        # Package initialization
    ├── translate_app.py   # Main Streamlit application
    ├── translation_service.py    # Google AI translation logic
    ├── audio_service.py           # Text-to-speech functionality
    ├── file_processors.py        # File extraction utilities
    └── ui_components.py           # UI rendering components
```

## 🔧 Dependencies

### Core Requirements
```txt
streamlit>=1.20.0          # Web application framework
google-generativeai>=0.2.0 # Google AI integration
python-dotenv>=1.0.0       # Environment variable management
gtts>=2.3.0                # Google Text-to-Speech
```

### File Processing
```txt
PyPDF2>=3.0.0              # PDF text extraction
python-docx>=0.8.11        # Word document processing
pandas>=1.5.0              # Excel/CSV processing
openpyxl>=3.0.0            # Excel file support
xlrd>=2.0.0                # Legacy Excel support
```

### Additional
```txt
langchain>=0.0.208         # AI workflow framework
chromadb>=0.3.23          # Vector database
watchdog>=3.0.0           # File monitoring
```

## 💡 Usage

### Text Input
1. Select "✍️ Type Text" option
2. Enter your text in the text area
3. Choose target language
4. Click "🔄 Start Processing"

### File Upload
1. Select "📁 Upload File" option
2. Upload supported file formats:
   - **TXT**: Plain text files
   - **PDF**: Portable Document Format
   - **DOCX**: Microsoft Word documents
   - **CSV**: Comma-separated values
   - **XLSX/XLS**: Excel spreadsheets
3. Preview extracted text
4. Choose target language
5. Click "🔄 Start Processing"

### Audio Generation
1. After successful translation
2. Translated text is Converted to Speech
3. Listen to generated audio
4. Download audio file (MP3 format)

## 🌍 Language Support
To add support for more languages, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes


## ⚙️ Configuration

### Environment Variables
```env
# Required
GOOGLE_API_KEY=your_api_key_here

# Optional
GENAI_MODEL=gemini-2.0-flash  # Default model to use
```

## 🚨 Troubleshooting

### Common Issues

#### 1. API Key Errors
```
❌ GOOGLE_API_KEY not found in environment variables
```
**Solution**: 
- Ensure `.env` file exists in project root
- Check API key is correctly formatted
- Regenerate API key if needed

#### 2. Quota Exceeded
```
Error: 429 You exceeded your current quota
```
**Solution**:
- Check usage limits in Google AI Studio
- Wait for quota reset (usually daily)
- Upgrade your Google AI plan
- Use shorter text inputs

#### 3. Model Not Found
```
Error: 404 models/gemini-pro is not found
```
**Solution**:
- Try different model name in `.env`
- Check model availability in your region
- Update `google-generativeai` package

#### 4. File Processing Errors
**Solution**:
- Ensure file format is supported
- Check file isn't corrupted
- Try smaller file sizes
- Verify file encoding (UTF-8 recommended)

### Debug Mode
Run the debug script to test your API configuration:
```bash
python debug_api.py
```

## 🔒 Security

### Important Security Notes
- **Never commit `.env` file** to version control
- **Keep API keys secure** and regenerate if compromised
- **Use environment variables** for sensitive data
- **Monitor API usage** to prevent unexpected charges

### Git Security
Ensure `.gitignore` includes:
```gitignore
# Environment variables
.env

# Python
__pycache__/
*.pyc
myenv/

# Streamlit
.streamlit/
```

## 🛠️ Development

### Adding New File Formats
1. Add extraction function in `file_processors.py`
2. Update `process_uploaded_file()` function
3. Add file type to upload widget in `ui_components.py`
4. Update requirements.txt if new dependencies needed

### Adding New Languages
1. Add language to `languages` dictionary in `ui_components.py`
2. Ensure gTTS supports the language code
3. Test translation and TTS functionality

### Customizing UI
- Modify `ui_components.py` for layout changes
- Update CSS in main app for styling
- Add new sections as needed

## 📄 License

This project is open source. Please check the license file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section
2. Run the debug script
3. Check your API quota and billing
4. Ensure all dependencies are installed
5. Verify file formats are supported

## 🔄 Version History

### v1.0.0
- Initial release
- Basic text translation
- File upload support
- Text-to-speech functionality
- Modular architecture

---

**Made with ❤️ using Streamlit and Google AI**