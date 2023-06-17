import speech_recognition as sr
import csv
import json
import requests

# Phase 2 su Projet python

def transcribe_audio(audio_file, lang):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    if lang == 'fr':
        return r.recognize_google(audio, language='fr-FR')
    elif lang == 'en':
        return r.recognize_google(audio, language='en-US')
    else:
        return "Language not supported"

def save_transcription(transcription, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([transcription])

def share_on_twitter(transcription):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    payload = {"status": transcription}
    headers = {'Authorization': 'Bearer YOUR_TOKEN'}
    requests.post(url, json=payload, headers=headers)

# example usage
audio_file = "path/to/audio.wav"
transcription = transcribe_audio(audio_file, "fr")
print(transcription)
save_transcription(transcription, "transcription.csv")
share_on_twitter(transcription)
