from gtts import gTTS
from django.shortcuts import render
from django.http import FileResponse
import os

def text_to_speech(request):
    if request.method == "POST":
        text = request.POST.get("text")
        voice_type = request.POST.get("voice")  # "male" or "female"
        speed = int(request.POST.get("speed", 140))  # Default speed

        # Set language (en for English) and create the speech
        language = 'en'
        tts = gTTS(text=text, lang=language, slow=False)
        
        # Save the audio file
        audio_file = "tts_output.mp3"
        tts.save(audio_file)

        return FileResponse(open(audio_file, 'rb'), as_attachment=True, content_type='audio/mpeg')

    return render(request, 'tts_app/index.html')
