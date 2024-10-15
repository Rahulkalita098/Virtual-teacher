import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import os

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    genai.configure(api_key="AIzaSyBQwpC_m4OGuDCiLqZcu5V1sv3uzQI0rbQ")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("please Do not use any kind of Symbols in your answer and give a good and robust answer."+command)
    return response.text

def processcommand(c):
        print("I am understanding your question........")
        output=aiprocess(c)
        speak(output)
        file_path = 'D:/Virtual teacher/write.txt'
        with open('D:/Virtual teacher/write.txt', 'w') as file:
            file.write(output + "\n")
        os.system(f'notepad {'D:/Virtual teacher/write.txt'}')
        
if __name__=="__main__":
    speak("Hello. I am your Virtual Teacher You can ask me any questions, You need help.")
    while True:
        r=sr.Recognizer()   
        print("I am Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listenning....")
                audio=r.listen(source,timeout=5,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="hello"):
                speak("Yes, Ask me anything you want ?")
                with sr.Microphone() as source:
                    print("I am listening....")
                    audio=r.listen(source, timeout=8, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    processcommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
