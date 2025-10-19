import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import os
from pathlib import Path
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Prescription OCR",
    page_icon="💊",
    layout="wide"
)

# Custom CSS for enhanced UI
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    .upload-box {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 2px 15px rgba(0,0,0,0.08);
        border: 2px dashed #e0e0e0;
        transition: all 0.3s ease;
    }
    .upload-box:hover {
        border-color: #667eea;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.15);
    }
    .result-box {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 2px 15px rgba(0,0,0,0.08);
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
    }
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.1);
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .sidebar .element-container {
        background: rgba(255, 255, 255, 0.05);
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Load API key from config
def load_api_key():
    """Load API key from config.py or environment variable"""
    try:
        from config import GEMINI_API_KEY
        return GEMINI_API_KEY
    except ImportError:
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            st.error("⚠️ API key not found. Please create a `config.py` file with your GEMINI_API_KEY or set it as an environment variable.")
            st.code("""# config.py
GEMINI_API_KEY = "your-api-key-here"
""", language="python")
            st.stop()
        return api_key

# Initialize Gemini
@st.cache_resource
def init_gemini(api_key):
    """Initialize Gemini API with caching"""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash-exp')

def extract_prescription_text(model, image):
    """Extract text from prescription image using Gemini"""
    prompt = """Analyze this handwritten medical prescription image and extract all information in a clean, structured format.

Please provide:
1. Patient Name (if visible)
2. Date (if visible)
3. Doctor's Name (if visible)
4. All medications with:
   - Medicine name
   - Dosage
   - Frequency
   - Duration
5. Any special instructions or notes

Format the output clearly and ensure all handwritten text is accurately transcribed. If any information is unclear or illegible, note it as [unclear]."""

    try:
        response = model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        return f"Error processing image: {str(e)}"

# Main app
def main():
    # Header with gradient
    st.markdown("""
        <div style='text-align: center; padding: 20px 0;'>
            <h1 style='color: #667eea; font-size: 3em; margin-bottom: 10px;'>💊 Prescription OCR</h1>
            <p style='color: #666; font-size: 1.2em; margin-bottom: 5px;'>Convert handwritten prescriptions into clean, machine-readable text</p>
            <p style='color: #999; font-size: 0.9em; font-style: italic;'>Made with ❤️ by Zaheer JK</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Load API key and initialize model
    api_key = load_api_key()
    model = init_gemini(api_key)
    
    # Sidebar with enhanced instructions
    with st.sidebar:
        st.markdown("### 📋 How to Use")
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 15px; border-radius: 10px; color: white; margin: 10px 0;'>
            <div style='display: flex; align-items: center; margin-bottom: 10px;'>
                <div style='background: white; color: #667eea; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 10px;'>1</div>
                <div><strong>Upload</strong><br/>Choose a prescription image</div>
            </div>
            <div style='display: flex; align-items: center; margin-bottom: 10px;'>
                <div style='background: white; color: #667eea; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 10px;'>2</div>
                <div><strong>Extract</strong><br/>Click to process with AI</div>
            </div>
            <div style='display: flex; align-items: center; margin-bottom: 10px;'>
                <div style='background: white; color: #667eea; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 10px;'>3</div>
                <div><strong>Review</strong><br/>Check extracted text</div>
            </div>
            <div style='display: flex; align-items: center;'>
                <div style='background: white; color: #667eea; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 10px;'>4</div>
                <div><strong>Download</strong><br/>Save as text file</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown("### 💡 Tips for Best Results")
        st.markdown("""
        ✅ **Good Lighting** - Natural light works best  
        ✅ **Clear Focus** - Avoid blurry images  
        ✅ **Full Capture** - Include entire prescription  
        ✅ **No Glare** - Avoid reflections and shadows  
        ✅ **High Resolution** - Use camera, not screenshots
        """)
        
        st.divider()
        
        st.markdown("### 📸 Supported Formats")
        st.markdown("JPG • JPEG • PNG • WebP")
        
        st.divider()
        
        st.markdown("### 🔒 Privacy Note")
        st.info("Images are processed through Google's Gemini API. Data is not stored permanently.")
    
    # File uploader in styled box
    st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "📤 Upload Prescription Image",
        type=['jpg', 'jpeg', 'png', 'webp'],
        help="Take a photo with your phone and upload it here"
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if uploaded_file is not None:
        # Two column layout
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.markdown("### 📸 Original Image")
            image = Image.open(uploaded_file)
            st.image(image, use_container_width=True)
            
            # Image metadata
            file_size = len(uploaded_file.getvalue()) / 1024
            st.markdown(f"""
                <div style='background: #f8f9fa; padding: 10px; border-radius: 8px; margin-top: 10px;'>
                    <small>
                    📏 <strong>Size:</strong> {image.size[0]}×{image.size[1]}px<br/>
                    📦 <strong>File Size:</strong> {file_size:.1f} KB<br/>
                    🖼️ <strong>Format:</strong> {image.format}
                    </small>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            st.markdown("### 📝 Extracted Text")
            
            # Process button
            if st.button("🔍 Extract Text", type="primary", use_container_width=True):
                with st.spinner("🔄 Processing prescription... This may take a few seconds"):
                    extracted_text = extract_prescription_text(model, image)
                    st.session_state.extracted_text = extracted_text
                    st.session_state.upload_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Display extracted text if available
            if 'extracted_text' in st.session_state:
                st.text_area(
                    "Extracted Prescription",
                    st.session_state.extracted_text,
                    height=350,
                    help="Copy this text for your records",
                    label_visibility="collapsed"
                )
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Action buttons
                col_btn1, col_btn2 = st.columns(2)
                
                with col_btn1:
                    # Prepare download content
                    download_content = f"""PRESCRIPTION OCR REPORT
{'='*50}

Extracted: {st.session_state.upload_time}
File: {uploaded_file.name}

{'='*50}

{st.session_state.extracted_text}

{'='*50}
Generated by Prescription OCR
Made by Zaheer JK
                    """
                    
                    st.download_button(
                        label="💾 Download Report",
                        data=download_content,
                        file_name=f"prescription_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col_btn2:
                    if st.button("🗑️ Clear Results", use_container_width=True):
                        del st.session_state.extracted_text
                        del st.session_state.upload_time
                        st.rerun()
            else:
                st.info("👆 Click 'Extract Text' to process the prescription")
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        # Empty state with helpful info
        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.info("👆 Upload a prescription image above to get started")
        
        with st.expander("ℹ️ How This Works", expanded=True):
            st.markdown("""
            **This application uses Google's Gemini AI to:**
            
            1. 🔍 **Analyze** handwritten prescription images
            2. 🧠 **Recognize** text using advanced OCR technology
            3. 📋 **Structure** information in a readable format
            4. ✅ **Extract** patient details, medications, and dosages
            
            **Perfect for:**
            - Digitizing paper prescriptions
            - Creating medication records
            - Archiving medical documents
            - Sharing prescriptions with pharmacies
            
            **Note:** Always verify extracted information with original documents before use.
            """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            <p style='color: #999; font-size: 0.9em;'>
                ⚠️ <strong>Disclaimer:</strong> This tool is for informational purposes only. 
                Always consult healthcare professionals before making medical decisions.
            </p>
            <p style='color: #999; font-size: 0.85em; margin-top: 10px;'>
                Made with ❤️ by <strong>Zaheer JK</strong> | Powered by Google Gemini AI
            </p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()