# Video in text converter
Python script that converts video to text using the speech_recognition library. 

You can specify the name of the mp4 file that you want to convert to text:
![image](https://github.com/StefKot/Video_to_Text_Converter/assets/96449266/8856079f-fece-4973-9322-48f3589b582f)

# Operating principle
* Converts mp4 to wav
* Calculates the duration of recording a digitized audio stream
* Opens a text file for recording, in which he writes the text received from the wav file, divided into intervals of a minute, from which noises are removed

## Installing the required library:
    Windows:
        pip install speech_recognition
    Linux:
        sudo apt install speech_recognition
