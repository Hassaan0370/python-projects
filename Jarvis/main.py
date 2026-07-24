import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import soundfile as sf
import webbrowser
from dotenv import load_dotenv
import os
from google import genai

r = sr.Recognizer()
load_dotenv()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def answer(question):
    try:
        mykey = os.getenv("API")
        client = genai.Client(api_key=mykey)

        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            input=f"{question} explain in short and act like jarvis (an AI voice assistant), try to complete in not more than two lines"
        )
        print(interaction.output_text)
        speak(interaction.output_text)
    except Exception as e:
        print (e)
        print("\nGemini API is busy or the quota has been exceeded. Please try again later.")
        speak("Gemini API is busy or the quota has been exceeded. Please try again later.")

def command():
    duration = 4
    samplerate = 16000

    print("Jarvis Active...")

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    sf.write("voice.wav", audio, samplerate)

    print("Recognizing...")


    with sr.AudioFile("voice.wav") as source:
        audio_data = r.record(source)

    try:
        text = r.recognize_google(audio_data)
        print(text)

        if(text.lower() == "open google"):
            webbrowser.open("https://www.google.com/")
        elif(text.lower() == "open youtube"):
            webbrowser.open("https://www.youtube.com/")
        elif(text.lower() == "open chatgpt"):
            webbrowser.open("https://www.chatgpt.com/")
        elif(text.lower() == "open gemini"):
            webbrowser.open("https://gemini.google.com/")
        else:
            answer(text)

    except sr.UnknownValueError:
        print("Can't understand.")

    except sr.RequestError as e:
        print("Error:", e)

if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        duration = 2
        samplerate = 16000

        print("listening...")

        audio = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        # Save audio
        sf.write("voice.wav", audio, samplerate)

        print("Recognizing...")


        with sr.AudioFile("voice.wav") as source:
            audio_data = r.record(source)

        try:
            text = r.recognize_google(audio_data)
            print(text)
            if(text.lower() == "jarvis"):
                speak("ya...")
                command()

        except sr.UnknownValueError:
            print("Can't understand.")

        except sr.RequestError as e:
            print("Error:", e)