"""
File processing utilities for text extraction from various file formats
"""
import pandas as pd
import PyPDF2
import docx
import streamlit as st


def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"


def extract_text_from_docx(docx_file):
    """Extract text from DOCX file"""
    try:
        doc = docx.Document(docx_file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        return f"Error reading DOCX: {e}"


def extract_text_from_txt(txt_file):
    """Extract text from TXT file"""
    try:
        # Try to decode as UTF-8 first, then fallback to other encodings
        try:
            content = txt_file.read().decode('utf-8')
        except UnicodeDecodeError:
            txt_file.seek(0)
            content = txt_file.read().decode('latin-1')
        return content.strip()
    except Exception as e:
        return f"Error reading TXT file: {e}"


def extract_text_from_csv(csv_file):
    """Extract text from CSV file"""
    try:
        # Try different encodings
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        df = None
        
        for encoding in encodings:
            try:
                csv_file.seek(0)  # Reset file pointer
                df = pd.read_csv(csv_file, encoding=encoding)
                break
            except UnicodeDecodeError:
                continue
        
        if df is None:
            return "Error: Could not read CSV file with any encoding"
        
        # Convert all data to string and combine
        text_parts = []
        
        # Add column headers
        text_parts.append("Column Headers: " + ", ".join(df.columns.astype(str)))
        text_parts.append("\n" + "="*50 + "\n")
        
        # Process each row
        for index, row in df.iterrows():
            row_text = []
            for col in df.columns:
                cell_value = str(row[col]) if pd.notna(row[col]) else ""
                if cell_value and cell_value.lower() != 'nan':
                    row_text.append(f"{col}: {cell_value}")
            
            if row_text:  # Only add non-empty rows
                text_parts.append(f"Row {index + 1}: " + " | ".join(row_text))
        
        return "\n".join(text_parts)
        
    except Exception as e:
        return f"Error reading CSV: {e}"


def extract_text_from_excel(excel_file):
    """Extract text from Excel file (XLSX)"""
    try:
        # Read all sheets
        excel_data = pd.read_excel(excel_file, sheet_name=None, engine='openpyxl')
        
        text_parts = []
        
        for sheet_name, df in excel_data.items():
            text_parts.append(f"\n{'='*20} SHEET: {sheet_name} {'='*20}")
            
            # Add column headers
            text_parts.append(f"Columns: {', '.join(df.columns.astype(str))}")
            text_parts.append("-" * 50)
            
            # Process each row
            for index, row in df.iterrows():
                row_text = []
                for col in df.columns:
                    cell_value = str(row[col]) if pd.notna(row[col]) else ""
                    if cell_value and cell_value.lower() != 'nan':
                        row_text.append(f"{col}: {cell_value}")
                
                if row_text:  # Only add non-empty rows
                    text_parts.append(f"Row {index + 1}: " + " | ".join(row_text))
            
            text_parts.append("")  # Add space between sheets
        
        return "\n".join(text_parts)
        
    except Exception as e:
        return f"Error reading Excel: {e}"


def process_uploaded_file(uploaded_file):
    """Process uploaded file and extract text"""
    if uploaded_file is not None:
        file_extension = uploaded_file.name.lower().split('.')[-1]
        
        if file_extension == 'pdf':
            return extract_text_from_pdf(uploaded_file)
        elif file_extension == 'docx':
            return extract_text_from_docx(uploaded_file)
        elif file_extension in ['txt', 'text']:
            return extract_text_from_txt(uploaded_file)
        elif file_extension == 'csv':
            return extract_text_from_csv(uploaded_file)
        elif file_extension in ['xlsx', 'xls']:
            return extract_text_from_excel(uploaded_file)
        else:
            return f"Unsupported file format: {file_extension}"
    return ""