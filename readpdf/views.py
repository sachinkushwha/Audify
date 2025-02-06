from django.shortcuts import render
from django.http import HttpResponse
from PyPDF2 import PdfReader
import pyttsx3
from io import BytesIO
import os

def upload_pdf(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']

        # Read the PDF file directly from memory (no saving required)
        pdf_file = BytesIO(file.read())  # Use in-memory storage
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        # Convert text to speech
        engine = pyttsx3.init()
        audio_file_path = os.path.join('static', 'output.mp3')  # Save to static directory
        engine.save_to_file(text, audio_file_path)
        engine.runAndWait()

        return render(request, 'index.html', {'audio_file_url': '/' + audio_file_path})

    return render(request, 'index.html')