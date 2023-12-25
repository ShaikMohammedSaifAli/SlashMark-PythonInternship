import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def assistant(query):
    if "hello" in query:
        speak("Hello! How can I help you?")
    elif "how are you" in query:
        speak("I'm doing well, thank you!")
    elif "what is your name" in query:
        speak("I am a voice assistant. You can call me Assistant.")
    elif "exit" in query:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Hello! I am your voice assistant.")
    
    while True:
        query = listen()
        assistant(query)
