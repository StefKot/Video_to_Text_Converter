import wave, math, contextlib
from alive_progress import alive_bar
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import os
from os import path

file_name = input("Enter the filename you want to convert to text (without file permissions): ")
# For video to wav audio
audio_file_name = file_name + ".wav"
video_file_name = file_name + ".mp4"

if (not os.path.isfile(audio_file_name)):
    audioclip = AudioFileClip(video_file_name)
    audioclip.write_audiofile(audio_file_name)


""" For mp3 audio to wav audio
sound = AudioSegment.from_mp3("04.mp3")
sound.export("transcript.wav", format="wav")
audio_file_name = "transcript.wav"
"""

with contextlib.closing(wave.open(audio_file_name,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
total_duration = math.ceil(duration / 60)
r = sr.Recognizer()

with open(file_name + ".txt", "w") as f:
    with alive_bar(total_duration) as bar:
        for i in range(total_duration):
            with sr.AudioFile(audio_file_name) as source:      
                r.adjust_for_ambient_noise(source) 
                audio = r.record(source, offset=i*60, duration=60)
                try:
                    f.write(str(r.recognize_google(audio, language="ru-RU", show_all=False)))
                    # print(r.recognize_google(audio, language="ru-RU", show_all=False))
                    f.write(" ")
                except Exception as e:
                    print(f"Exception: {e}\nDuration: {i}")
                bar()
            
