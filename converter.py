import wave, math, contextlib
from alive_progress import alive_bar
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from os import path

file_name = input("Enter the filename you want to convert to text (without file permissions): ")
# For video to wav audio
audio_file_name = file_name + ".wav"
video_file_name = file_name + ".mp4"

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
f = open(file_name + ".txt", "w")


with alive_bar(total_duration) as bar:
    for i in range(total_duration):
        with sr.AudioFile(audio_file_name) as source:       
            audio = r.record(source, offset=i*20, duration=20)
            f.write(r.recognize_google(audio, language="ru-RU"))
            f.write(" ")
            bar()
            
    f.close()
