import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os # use for the music
# pip install pyaudio, speechRecognition, pyttsx3 , wikipedia
# sapi5 this API take an inbuilt voice
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# check the voices initially there are  two voices we can see into the terminal by using the print(voices)
#print(voices)
#print(voices[1].id) the voice of female
#print(voices[0].id) the voice of male
engine.setProperty('voice',voices[1].id)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        Speak('Good Morning!')
    elif(hour>=12 and hour<18):
        Speak("Good Afternoon")
    else:
        Speak("Good Evening")
    Speak("Hey I am Dora, How may I help you?")

def takeCommand():
    # It takes microphone input and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold=1 # gap between the word while speaking
        audio=r.listen(source) #  press ctrl and click that function it will shows the features of that functions
    try:
        print("Recognizing...")    
        query=r.recognize_google(audio,language='en-in')
        print(f"User said {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please!!!")
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:

        
    #if 1:

        query=takeCommand().lower()
        if('wikipedia' in query):
            Speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2) # It will speak the first two sentences
            Speak('According to wikipedia')
            Speak(results)
        elif("open youtube" in query):
            webbrowser.open('Youtube.com')
        elif("open google" in query):
            webbrowser.open("Google.com")
        elif("play music" in query):
            music_dir="C:\\Users\\admin\\Music\\Bhole song"
            songs=os.listdir(music_dir)
            print(songs)
            # we can also use the random module to play the song randomly
            os.startfile(os.path.join(music_dir,songs[0]))
        elif("play movies" in query):
            path="C:\\Users\\admin\\Videos\\Movie"
            os.startfile(path)
        elif("open chrome browser" in query):
            path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif("open Microsoft Edge browser" in query):
            path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(path)
        elif("the time" in query):
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strTime}")
        elif("open code" in query):
            path="C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif("open ms word" in query):
            path="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path)
        elif("open ms excel" in query):
            path="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(path)
        elif("open ms powerpoint" in query):
            path="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path)
        elif("thank you" in query):
            Speak("welcome dear")
            break

        