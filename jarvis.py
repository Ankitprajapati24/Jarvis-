import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning !")
    elif hour<=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
    
    speak('HELLO Ankit sir')
    speak('I am jarvis')
    speak('Please tell me how may i help you')
    speak("today... words..are")
    speak('if you remove! I and M from IMPOSSIBAL ! then every thing will be POSSIBAL for you!')


def takeCommamd():
    # it take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, languageg='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("say it again Please ")
        return "None"
    return query

if __name__ == "__main__": 
    # speak("Hello Ankit sir !")
    wishMe()
    while True:
        query = takeCommamd().lower()
        # logic for executing task based on queary 
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=5)
            speak('According to wikipedia')
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\vbardhamnamn\\Desktop\\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strTime}")

        elif ' open code' in query:
            codePath = "C:\\Users\\vbardhamnamn\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)