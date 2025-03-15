import time
from gtts import gTTS
from django.http import FileResponse
from django.shortcuts import render
import os
import requests

def text_to_speech(request):
    if request.method == "POST":
        text = request.POST.get("text")
        voice_type = request.POST.get("voice")  # "male" or "female"
        speed = int(request.POST.get("speed", 140))  # Default speed (WPM)

        # Set language (en for English) and create the speech
        language = 'en'
        slow = False  # Default to False (normal speed)
        if speed < 100:
            slow = True  # Slow down if speed is below 100

        # Retry logic
        retries = 3
        delay = 2  # seconds between retries
        for i in range(retries):
            try:
                tts = gTTS(text=text, lang=language, slow=slow)
                audio_file = "tts_output.mp3"
                tts.save(audio_file)
                return FileResponse(open(audio_file, 'rb'), as_attachment=True, content_type='audio/mpeg')
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 429:
                    # Wait before retrying if rate limit is hit
                    time.sleep(delay)
                    continue  # Retry the request
                else:
                    raise e  # Raise the exception if it's not a 429
        return render(request, 'tts_app/index.html', {"error": "Rate limit exceeded. Please try again later."})

    return render(request, 'tts_app/index.html')
