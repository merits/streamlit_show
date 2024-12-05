import streamlit as st
#import pyttsx3

# 챗봇 응답을 생성하는 함수
def get_chatbot_response(user_input):
    # 여기에서 실제로 챗봇의 응답 로직을 구현할 수 있습니다.
    return f"챗봇: '{user_input}'에 대한 답변입니다."

# TTS (Text-to-Speech) 함수
#def text_to_speech(text):
#    engine = pyttsx3.init()
#    engine.say(text)
#    engine.runAndWait()

# HTML과 JavaScript를 사용하여 음성 인식
html_code = """
<script>
  function startRecognition() {
    var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'ko-KR';
    recognition.onstart = function() { 
        document.getElementById("status").innerHTML = "음성 인식 시작...";
    };
    recognition.onresult = function(event) {
        var transcript = event.results[0][0].transcript;
        document.getElementById("result").innerHTML = "사용자: " + transcript;
        // Python Streamlit에 음성 인식 결과를 전달
        window.parent.postMessage({text: transcript}, "*");
    };
    recognition.onerror = function(event) {
        document.getElementById("status").innerHTML = "음성 인식 에러: " + event.error;
    };
    recognition.start();
  }
</script>

<button onclick="startRecognition()">음성 인식 시작</button>
<p id="status">음성 인식 대기 중...</p>
<p id="result"></p>
"""

# Streamlit 앱의 메인 화면
def main():
    st.title("음성 대화 챗봇")

    # 음성 인식을 위한 HTML 삽입
    st.components.v1.html(html_code)

    # 음성 인식 결과를 처리
    user_input = st.text_input("사용자 음성 입력:")

    if user_input:
        st.text(f"사용자: {user_input}")
        chatbot_response = get_chatbot_response(user_input)
        st.text(chatbot_response)    
        # TTS (Text-to-Speech)
        #text_to_speech(chatbot_response)

if __name__ == "__main__":
    main()



'''
import streamlit as st

def main():
    st.title("타이핑 챗봇")

    # 챗봇 응답을 얻는 함수
    def get_chatbot_response(user_input):
        # 여기에서 실제로 챗봇의 응답 로직을 구현할 수 있습니다.
        # 예를 들어, 간단하게 사용자 입력에 대한 답변을 생성할 수 있습니다.
        return f"챗봇: '{user_input}'에 대한 답변입니다."

    user_input = st.text_input("사용자 입력:")
    
    if st.button("대화하기"):
        chatbot_response = get_chatbot_response(user_input)
        st.text(chatbot_response)

if __name__ == "__main__":
    main()
'''


'''
import streamlit as st
import speech_recognition as sr
import pyttsx3


def main():
    st.title("음성 대화 챗봇")

    # 음성 입력을 위한 함수
    def get_audio_input():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            audio = r.listen(source)

        # 구글 웹 음성 API로 인식하기 
        try:
            print("Google Speech Recognition thinks you said : " + r.recognize_google(audio, language='ko'))
            return r.recognize_google(audio, language='ko')
        except sr.UnknownValueError as e:
            print("Google Speech Recognition could not understand audio".format(e))
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None


    # 챗봇 응답을 얻는 함수
    def get_chatbot_response(user_input):
        # 여기에서 실제로 챗봇의 응답 로직을 구현할 수 있습니다.
        return f"챗봇: '{user_input}'에 대한 답변입니다."

    user_input = st.text_input("사용자 음성 입력:")

    # TTS 
    def text_to_speech(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    

    if st.button("마이크 켜기"):
        user_input = get_audio_input()
        if user_input is not None:
            st.text(f"사용자: {user_input}")
            chatbot_response = get_chatbot_response(user_input)
            st.text(chatbot_response)    
            # TTS api
            text_to_speech(chatbot_response)

if __name__ == "__main__":
    main()
'''


'''
import streamlit as st

col1,col2 = st.columns([2,3])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

with col1 :
  # column 1 에 담을 내용
  st.title('here is column1')
with col2 :
  # column 2 에 담을 내용
  st.title('here is column2')
  st.checkbox('this is checkbox1 in col2 ')


# with 구문 말고 다르게 사용 가능 
col1.subheader(' i am column1  subheader !! ')
col2.checkbox('this is checkbox2 in col2 ') 
#=>위에 with col2: 안의 내용과 같은 기능을합니다
'''

'''
import streamlit as st

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

with tab1:
  #tab A 를 누르면 표시될 내용
  st.write('hello')
    
with tab2:
  #tab B를 누르면 표시될 내용 
  st.write('hi')
'''

'''
import streamlit as st

#st.sidebar는 

st.sidebar.title('this is sidebar')
st.sidebar.checkbox('체크박스에 표시될 문구')
# 사이드바에 체크박스, 버튼등 추가할 수 있습니다! 
'''


'''
import streamlit as st
from PIL import Image

#PIL 패키지에 이미지 모듈을 통해 이미지 열기 
# Image.open('이미지 경로')
zarathu_img = Image.open('zarathu.png')

col1,col2 = st.columns([2,3])

with col1 :
  # column 1 에 담을 내용
  st.title('here is column1')
with col2 :
  # column 2 에 담을 내용
  st.title('here is column2')
  st.checkbox('this is checkbox1 in col2 ')


# 컬럼2에 불러온 사진 표시하기
col2.image(zarathu_img)
'''

