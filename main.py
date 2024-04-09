import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
import datetime
from config import apikey
import random
import wikipedia
import pyttsx3 as p

def ai(prompt):
    # openai.api_key = apikey
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n ***************\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "prompt"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response["choices"][0]["message"]["content"])
    text += (response["choices"][0]["message"]["content"])

    # if not os.path.exists("Openai"):
    #     os.mkdir("Openai")
    #
    # with open(f"Openai/prompt- {random.randint(1, 535185499)}") as f:
    #     f.write(text)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred, Sorry..."


if __name__ == '__main__':
    print('PyCharm')
    say("Hello I'm KEETO AI")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [['youtube', "https://www.youtube.com/"], ["wikipedia", "https://www.wikipedia.com/"],
                 ["google", "https://www.google.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f'Opening {site[0]} maam...')
                webbrowser.open(site[1])

            if "the time" in query:
                strftime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"maam the time is {strftime}")

            if "using ai".lower() in query.lower():
                ai(prompt=query)

            if 'wikipedia' in query:
                p.speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                p.speak("According to Wikipedia")
                print(results)
                p.speak(results)

            if "hello" in query:
                p.speak("hello Mam, i am jarvis ")
                p.speak("i am your ai assistant")                                    
                p.speak("how can i help you ")
                break
            elif "how are you " in query:
                p.speak(" i am fine sir thank you for asking")
                break
            elif "bye" in query:
                p.speak("have a good day ahead")
                break

            if "using ai".lower() in query.lower():
                ai(prompt=query)
                break


