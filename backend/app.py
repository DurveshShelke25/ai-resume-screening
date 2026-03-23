from flask import Flask, request, jsonify
from flask_cors import CORS
from model import match_resume
import PyPDF2

app = Flask(__name__)
CORS(app)

# 📄 Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

@app.route('/')
def home():
    return "Server is running with PDF support ✅"

# 📄 NEW API for PDF upload
@app.route('/upload', methods=['POST'])
def upload():
    job_desc = request.form['job_desc']
    file = request.files['resume']

    resume_text = extract_text_from_pdf(file)

    result = match_resume(job_desc, resume_text)

    return jsonify(result)

if __name__ == '__main__':
    print("Server starting...")
    app.run(debug=True)