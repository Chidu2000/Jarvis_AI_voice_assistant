import smtplib  #for sending emails
import pyttsx3  #py library for text to speech conversion
import speech_recognition as sr 
import pyaudio
import datetime
import wikipedia
import webbrowser
import os  

engine = pyttsx3.init('sapi5')  #sapi5 -> microsoft's speech API
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def WishMe():
    time = int(datetime.datetime.now().hour) 
    if time>=0 and time<12:
        speak("Good morning")
        
    elif time>=12 and time<18:
        speak("Good afternoon")
        
    else:
        speak("Good evening")
        
    speak("I am jarvis sir. Tell me how may I help you")   
    
def takeCommand():
    # it takes mic input from the user and return string o/p
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)   
        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('chidambarvjoshi@gmail.com','your-password')
    server.sendmail('chidambarvjoshi@gmail.com',to,content)
    server.close()
    
if __name__ == "__main__":
    # speak('Chidambar is Handsome')   
    WishMe() 
    while True:
        query = takeCommand().lower()
        
        
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  
            
        elif 'play music' in query:
            music_dir = 'G:\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"Sir,The time is {strTime}") 
            
        elif 'the code' in query:
            codePath = "G:\\PROJECTS\\Jarvis AI desktop voice assisstant\\"
            os.startfile(codePath)
            
        elif 'email to chidu' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "chidambarvjoshi@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak('The send email is unsuccessfull')  
                                     