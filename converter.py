import wave, math, contextlib
from alive_progress import alive_bar
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import os
from os import path

import config

# Noise Reduction Control parameter
NOISE = False 


file_name = input("Enter the filename you want to convert to text (without file permissions): ")

# Creating directories for mp4, wav and txt files
if (not os.path.exists(config.mp4_path)):
    os.mkdir(config.mp4_path)

if (not os.path.exists(config.wav_path)):
    os.mkdir(config.wav_path)

if (not os.path.exists(config.txt_path)):
    os.mkdir(config.txt_path)

# For video to wav audio
audio_file_name = os.path.join(config.wav_path, file_name + ".wav")
video_file_name = os.path.join(config.mp4_path, file_name + ".mp4")

# Checking the existence of a wav file, for re-processing into a txt file
if (not os.path.isfile(audio_file_name)):
    audioclip = AudioFileClip(video_file_name)
    audioclip.write_audiofile(audio_file_name)

""" For mp3 audio to wav audio
sound = AudioSegment.from_mp3("04.mp3")
sound.export("transcript.wav", format="wav")
audio_file_name = "transcript.wav"
"""

with contextlib.closing(wave.open(audio_file_name, 'r')) as file:
    frames = file.getnframes()
    rate = file.getframerate()
    duration = frames / float(rate)
total_duration = math.ceil(duration / 60)
record = sr.Recognizer()

with open(os.path.join(config.txt_path, file_name + ".txt"), "w") as file:
    with alive_bar(total_duration) as bar:
        for i in range(total_duration):
            with sr.AudioFile(audio_file_name) as source: 
                if NOISE:    
                    record.adjust_for_ambient_noise(source) 
                audio = record.record(source, offset=i*60, duration=60)
                try:
                    file.write(str(record.recognize_google(audio, language="ru-RU", show_all=False)))
                    file.write(" ")
                except Exception as e:
                    print(f"Exception: {e}\nDuration: {i}")
                bar()
            
