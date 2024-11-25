import streamlit as st
import pyttsx3
import streamlit.components.v1 as components
from streamlit_webrtc import webrtc_streamer, WebRtcMode

# 챗봇 응답을 얻는 함수
def get_chatbot_response(user_input):
    # 여기에서 실제로 챗봇의 응답 로직을 구현할 수 있습니다.
    return f"챗봇: '{user_input}'에 대한 답변입니다."

# TTS 기능
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Streamlit 웹 앱
def main():
    st.title("음성 대화 챗봇")

    user_input = None

    # '마이크 켜기' 버튼 클릭 시 음성 입력 받기
    if st.button("마이크 켜기"):
        # JavaScript로 마이크 입력 받기
        st.header("마이크 입력")
        components.html("""
            <script>
                const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
                recognition.lang = "ko-KR"; // 한국어
                recognition.interimResults = true;
                recognition.maxAlternatives = 1;

                recognition.onresult = function(event) {
                    const userSpeech = event.results[0][0].transcript;
                    // 결과를 스트림릿으로 전송
                    window.parent.postMessage({func: 'update_text', text: userSpeech}, '*');
                };

                recognition.onerror = function(event) {
                    console.error("음성 인식 오류: " + event.error);
                };

                recognition.start();
            </script>
        """, height=300)

    # 음성 인식된 텍스트 받기
    message = st.empty()
    if st.session_state.get('user_input'):
        user_input = st.session_state['user_input']
        message.text(f"사용자: {user_input}")
        chatbot_response = get_chatbot_response(user_input)
        st.text(chatbot_response)
        # TTS (Text to Speech)
        text_to_speech(chatbot_response)

    # WebRTC 설정을 위한 코드 (마이크 사용)
    st.header("실시간 오디오 스트리밍")
    webrtc_streamer(key="example", audio_receiver_size=256, mode=WebRtcMode.SENDRECV)

if __name__ == "__main__":
    main()

# JavaScript와 Streamlit 통합을 위한 코드 (마이크 입력)
# 아래 코드로 음성 입력을 스트리밍한 후 이를 텍스트로 변환하여 챗봇에 전달할 수 있습니다.

import streamlit as st

# 메시지 처리
def update_text_from_js(message):
    if message.get('func') == 'update_text':
        st.session_state['user_input'] = message.get('text')

# JavaScript에서 전송된 메시지 처리
st.components.v1.html("""
    <script>
        window.addEventListener('message', (event) => {
            if (event.data.func === 'update_text') {
                const userInput = event.data.text;
                // Send user input to Python backend
                parent.postMessage({func: 'update_text', text: userInput}, '*');
            }
        });
    </script>
""")


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

