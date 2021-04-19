import pyttsx3
import speech_recognition as sr
import webbrowser
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

songs = [
    "https://www.youtube.com/watch?v=bBNpSXAYteM",
    "https://www.youtube.com/watch?v=tvTRZJ-4EyI&ab_channel=KendrickLamar",
    "https://youtu.be/glaG64Ao7sM",
    "https://youtu.be/hRK7PVJFbS8",
    "https://youtu.be/NLZRYQMLDW4",
]

query = ""

facts = [
    "Kendrick Lamar was born on 17th June 1987 - making the rapper 30 years old!",
    "Kendrick Lamar is among the shortest rappers in Hip-Hop, standing at 5 feat 6 inches.",
    "Kendrick Lamar and Kanye West famously collaborated on album The Life Of Pablo. Kanye released a song called No More Parties In LA alongside Kendrick, then later admitted the pair have more than 40 songs together. However more songs are yet to surface.",
    "Kendrick Lamar and Big Seans beef appeared to start after the pair collaborated on a song called Control. Kendrick dissed a number of rappers including Big Sean - on his own song! Since that moment the rappers have sent a series of subliminal disses to each other in a number of songs.",
    "Kendrick Lamar and TDE released the official soundtrack for the Black Panther movie on 9th February 2018. The project features collaborations with The Weekend, Travis Scott, Future and more.",
    "Kendrick Lamars best commercially performing songs include HUMBLE, Alright, Swimming Pools, i and DNA. However the rappers discography is filled with huge songs.",
    "Kendrick Lamar is actually from Compton, Los Angeles. However the rapper has now travelled the world thanks to his hugely successful career.",
    "Dr Dre tracked Lamar down after hearing the song Ignorance Is Bliss - the standout track from the rappers mixtape Overly Addicted.",
    "His real name is Kendrick Lamar Duckworth",
    "He won Best Rap Song in both 2015 and 2016, and won Best Rap Album in 2016 for To Pimp A Butterfly.",
    "Kendrick attended the same school as Dr. Dre. The rappers credentials go back a long way - he attended Centennial High School in Compton, the same school as Dr Dre. Lamar was a straight A student during his time at the school.",
    'Lady Gaga is a big fan. Its official, Lamars biggest fan is Lady Gaga and, at one point, it looked as though Mother Monster might have a track on Lamars debut album Good Kid, MAAD City. The admiration is mutual, with Lamar describing Lady Gaga as a "beautiful person".',
    "Kendrick really loves sugary cereal. The song Cartoon And Cereal isnt called that for nothing. Kendrick loves cereal, but dont get him started on the healthy cereals! You pick that up in the aisle and you come talk to me, Im liable to punch you in the face if youre my cousin, he joked.",
]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
        except:
            print("Say that again please...")
            query = None
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand()
        if query != None:
            if "Kendrick" in query:
                if "play" in query:
                    speak("playing kendrick lamar")
                    webbrowser.open(songs[random.randint(0, len(songs) - 1)], new=2)
                else:
                    speak(facts[random.randint(0, len(facts) - 1)])
