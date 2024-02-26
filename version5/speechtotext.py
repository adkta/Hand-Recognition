import speech_recognition as sr

r= sr.Recognizer()

def record_text():
    while(True):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=1)
                audio2= r.listen(source2)
                print("Audio captured:", audio2)
                myText= r.recognize_google(audio2, language= "ne-NP")
                return myText
        except AttributeError as e:
            print("AttributeError: {}".format(e))
        except sr.RequestError as e:
            print("could not request results: {0}".format(e))
        except sr.UnknownValueError as e:
            print("UnknownValueError: {0}".format(e))

def output_text(text):
    f= open("output.txt",'a', encoding="utf-8")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text= record_text()
    output_text(text)
    print(format(text))

    print("Wrote text")