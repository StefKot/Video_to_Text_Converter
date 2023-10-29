# Video in text converter
Python script that converts video to text using the speech_recognition library. 

You can specify the name of the mp4 file that you want to convert to text:
![image](https://github.com/StefKot/Video_to_Text_Translator/assets/96449266/dca2e4b0-be02-4fc6-8dba-d61b53f9b239)
# Operating principle
* Converts mp4 to wav
* Calculates the duration of recording a digitized audio stream
* Opens a text file for recording, in which he writes the text received from the wav file, divided into intervals of a minute, from which noises are removed.

## Installing the required library:
    Windows:
        pip install speech_recognition
    Linux:
        sudo apt install speech_recognition
