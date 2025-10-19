# 💊 Prescription OCR

**Made with ❤️ by Zaheer JK**

A powerful Streamlit-based web application that converts handwritten medical prescriptions into clean, machine-readable text using Google's Gemini AI technology.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- 🔍 **AI-Powered OCR**: Utilizes Google's Gemini 2.0 Flash model for accurate text extraction
- 📝 **Structured Output**: Extracts patient details, medications, dosages, and instructions
- 🎨 **Beautiful UI**: Modern gradient design with smooth animations and transitions
- 📸 **Multiple Formats**: Supports JPG, JPEG, PNG, and WebP image formats
- 💾 **Export Reports**: Download extracted text as formatted text files
- 🔒 **Privacy Focused**: Images processed securely through Google's API
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- ⚡ **Fast Processing**: Quick analysis with real-time feedback

## 🎯 Use Cases

- Digitizing paper prescriptions for electronic health records
- Creating searchable medication databases
- Archiving medical documents
- Sharing prescriptions with online pharmacies
- Maintaining personal health records
- Assisting healthcare professionals with data entry

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API Key
- Modern web browser

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <https://github.com/Tensor-Titans-Labs/Prescription_OCR.git>
cd prescription-ocr
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `config.py` file in the project root:

```python
# config.py
GEMINI_API_KEY = "your-gemini-api-key-here"
```

**Alternative:** Set as environment variable:

```bash
export GEMINI_API_KEY="your-gemini-api-key-here"
```

Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 💻 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Step-by-Step Guide

1. **Upload**: Click the upload area and select a prescription image
2. **Extract**: Click the "Extract Text" button to process the image
3. **Review**: Check the extracted text for accuracy
4. **Download**: Save the report as a text file for your records

## 📸 Tips for Best Results

✅ **Good Lighting** - Use natural light or bright, even lighting  
✅ **Clear Focus** - Ensure the prescription is sharp and in focus  
✅ **Full Capture** - Include the entire prescription in the frame  
✅ **No Glare** - Avoid reflections and shadows on the paper  
✅ **High Resolution** - Take photos with your camera, not screenshots  
✅ **Flat Surface** - Place prescription on a flat surface for capture

## 🗂️ Project Structure

```
prescription-ocr/
│
├── app.py                  # Main Streamlit application
├── config.py              # API key configuration (not in git)
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
```

## 🔧 Configuration

The application uses the following settings:

- **AI Model**: gemini-2.0-flash-exp
- **Supported Image Formats**: JPG, JPEG, PNG, WebP
- **Max Image Size**: Limited by Streamlit's default (200MB)
- **Layout**: Wide mode for better visualization

## 🎨 Features Breakdown

### Image Processing
- Real-time image preview with metadata display
- Shows image dimensions, file size, and format
- Handles various image formats and sizes

### Text Extraction
- Extracts patient name, date, and doctor's name
- Identifies medications with dosage, frequency, and duration
- Captures special instructions and notes
- Marks unclear or illegible text

### Export Options
- Timestamped reports with extraction details
- Well-formatted text files
- Includes original filename and processing date

## 🔒 Privacy & Security

- Images are processed through Google's Gemini API
- No images or data are stored permanently on our servers
- API calls are made over secure HTTPS connections
- User data is handled according to Google's privacy policy

## ⚠️ Important Disclaimer

**Medical Disclaimer**: This tool is for informational and educational purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always:

- Verify extracted information with the original prescription
- Consult healthcare professionals for medical decisions
- Keep original prescriptions as legal documents
- Use extracted text as a reference only

## 🛠️ Troubleshooting

### Common Issues

**API Key Error**
```
Solution: Ensure config.py exists with valid GEMINI_API_KEY
```

**Image Upload Fails**
```
Solution: Check image format (JPG, PNG, WebP) and file size
```

**Text Extraction Error**
```
Solution: Verify API quota, internet connection, and image clarity
```

**App Won't Start**
```
Solution: Check Python version (3.8+) and reinstall dependencies
```

## 🚧 Future Enhancements

- [ ] Multi-language support for international prescriptions
- [ ] Batch processing for multiple prescriptions
- [ ] Database integration for prescription history
- [ ] Mobile app version (iOS/Android)
- [ ] Integration with pharmacy APIs
- [ ] PDF export with formatting
- [ ] Voice-to-text prescription notes
- [ ] Medicine interaction checker
- [ ] Reminder system for medication schedules

## 📊 Technology Stack

- **Frontend**: Streamlit with custom CSS
- **AI/ML**: Google Gemini 2.0 Flash
- **Image Processing**: PIL (Pillow)
- **Language**: Python 3.8+

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Zaheer JK**

- Made with passion for healthcare innovation
- Powered by cutting-edge AI technology

## 🙏 Acknowledgments

- Google for providing the Gemini AI API
- Streamlit team for the amazing framework
- Healthcare professionals who inspired this project
- Open-source community for continuous support

## 📞 Support

For questions, issues, or feature requests:
- Open an issue in the repository
- Check existing documentation
- Review troubleshooting section

## 🔗 Useful Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Python Pillow Documentation](https://pillow.readthedocs.io/)

---

<div align="center">
  <p>Made with ❤️ by <strong>Zaheer JK</strong></p>
  <p>⭐ Star this repo if you find it useful!</p>

</div>
