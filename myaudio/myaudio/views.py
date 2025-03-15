import pyttsx3
from django.shortcuts import render
from django.http import FileResponse
import os

def text_to_speech(request):
    if request.method == "POST":
        text = request.POST.get("text")
        voice_type = request.POST.get("voice")  # "male" or "female"
        speed = int(request.POST.get("speed", 140))  # Default speed 140 WPM

        # Initialize pyttsx3 engine
        engine = pyttsx3.init()

        # Get available voices
        voices = engine.getProperty('voices')

        # Set voice based on user selection
        if voice_type == "male":
            engine.setProperty('voice', voices[0].id)  # Male voice
        elif voice_type == "female":
            engine.setProperty('voice', voices[1].id)  # Female voice

        # Set speech speed
        engine.setProperty('rate', speed)  

        # Save the audio file
        audio_file = "tts_output.mp3"
        engine.save_to_file(text, audio_file)
        engine.runAndWait()

        # Serve the audio file as a response
        return FileResponse(open(audio_file, 'rb'), as_attachment=True, content_type='audio/mpeg')

    return render(request, 'tts_app/index.html')
