import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
from email.message import EmailMessage


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query} ")

    except Exception as e:
        speak("say that again please")
        return "none"
    return query

def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")

    elif hour>12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("I am a virtual voice assistant Please tell me how can i help you")

def sendEmail(receiver,subject,messasge):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('it224002@saranathan.ac.in','AbimanyuT02')
    email=EmailMessage()
    email['From']='it224004@saranathan.ac.in'
    email['To']=receiver
    email['Subject']=subject
    email.set_content(messasge)
    server.send_message(email)
    server.close()

email_list={'abi':'abimanyumahesh795@gmail.com'}


if __name__=="__main__":
    wish()
    #while True:
    if 1:

        query=takecommand().lower()

        if "open notepad" in query:
            npath="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir="C:\\Users\\Abi\\Music"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime} ")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        
        elif "open google" in query:
            speak("sir,what should i search on google")
            cm=takecommand().lower()
            webbrowser.open((f"{cm}"))

        elif "email" in query:
            try:
                speak("To whom you want to send email")
                name=takecommand()
                receiver=email_list[name]
                print(receiver)
                speak("what is the subject of your email")
                subject=takecommand()
                print(subject)
                speak("Tell me text in your email")
                message=takecommand()
                print(message)
            

            except:
                speak("Sorry my friend.I am not able to send this email")
            sendEmail(receiver,subject,message)


        elif "no thanks" in query:
            speak("thanks for using me sir,have a good day")
            sys.exit()
        
        