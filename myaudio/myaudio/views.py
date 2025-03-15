from gtts import gTTS
from django.shortcuts import render
from django.http import FileResponse
import os

def text_to_speech(request):
    if request.method == "POST":
        text = request.POST.get("text")
        voice_type = request.POST.get("voice")  # "male" or "female"
        speed = int(request.POST.get("speed", 140))  # Default speed (WPM)

        # Set language (en for English) and create the speech
        language = 'en'
        
        # Set the speed (slow=True for slower speech, slow=False for normal speed)
        slow = False  # Default to False (normal speed)
        if speed < 100:
            slow = True  # Slow down if speed is below 100

        # Create the gTTS object
        tts = gTTS(text=text, lang=language, slow=slow)
        
        # Save the audio file
        audio_file = "tts_output.mp3"
        tts.save(audio_file)

        return FileResponse(open(audio_file, 'rb'), as_attachment=True, content_type='audio/mpeg')

    return render(request, 'tts_app/index.html')
