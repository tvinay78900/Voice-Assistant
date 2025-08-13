import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sys

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speaking speed

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that. Can you repeat?")
        return ""
    except sr.RequestError:
        speak("Sorry, I am having trouble connecting.")
        return ""
    return command

def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you today?")

def perform_task(command):
    if "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time_now}")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("What would you like to search for?")

    elif "hello" in command or "hi" in command:
        speak("Hello there! What can I do for you?")

    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye!")
        sys.exit()

    else:
        speak("Sorry, I don't understand that command yet.")

# Main Program
if __name__ == "__main__":
    greet_user()
    while True:
        user_command = listen()
        if user_command:
            perform_task(user_command)