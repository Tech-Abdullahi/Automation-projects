import SpeechRecognition as sr
import webbrowser

r = sr.Recognizer()


with sr.microphone() as source:
    print("what you want to search\n")
    audio = r.listen(source)


print('opening:' + r.recognize_google(audio))



p = r.recognize_google(audio)
webbrowser.open(p)

