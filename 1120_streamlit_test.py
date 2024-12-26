import speech_recognition as sr

# microphone에서 auido source를 생성합니다
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# 구글 웹 음성 API로 인식하기 
try:
    print("Google Speech Recognition thinks you said : " + r.recognize_google(audio, language='ko'))
except sr.UnknownValueError as e:
    print("Google Speech Recognition could not understand audio".format(e))
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
