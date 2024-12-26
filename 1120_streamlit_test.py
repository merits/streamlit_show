import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    input_text = input("Enter the text to convert to speech: ")
    text_to_speech(input_text)
