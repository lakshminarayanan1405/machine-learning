import speech_recognition as sr
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print("Calibrating for bg noise....pls wait")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("speak something")
    audio=recognizer.listen(source)

try:
    text=recognizer.recognize_google(audio,language="en-US")
    print("you said:",text)
except sr.UnknownValueError:
    print("could not understand your audio")
except sr.RequestError as e:
    print("pls try again",e)
