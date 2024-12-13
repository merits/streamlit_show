import streamlit as st

def get_chatbot_response(user_input):
    # 기존 챗봇 로직을 유지하면서 음성 인식 결과 처리
    return f"챗봇: '{user_input}'에 대한 답변입니다."

# 개선된 음성 인식 JavaScript 코드
html_code = """
<script>
let recognition;
let isRecording = false;

function toggleRecognition() {
    if (!isRecording) {
        startRecognition();
    } else {
        stopRecognition();
    }
}

function startRecognition() {
    recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'ko-KR';
    recognition.continuous = true;
    recognition.interimResults = true;
    
    recognition.onstart = function() {
        isRecording = true;
        document.getElementById("status").innerHTML = "음성 인식 중...";
        document.getElementById("voiceButton").innerHTML = "음성 인식 중지";
        document.getElementById("voiceButton").classList.add("recording");
    };
    
    recognition.onresult = function(event) {
        let finalTranscript = '';
        let interimTranscript = '';
        
        for (let i = event.resultIndex; i < event.results.length; i++) {
            const transcript = event.results[i][0].transcript;
            if (event.results[i].isFinal) {
                finalTranscript += transcript;
            } else {
                interimTranscript += transcript;
            }
        }
        
        document.getElementById("result").innerHTML = 
            "사용자: " + finalTranscript + 
            '<div style="color: gray;">' + interimTranscript + '</div>';
            
        if (finalTranscript) {
            window.parent.postMessage({text: finalTranscript}, "*");
        }
    };
    
    recognition.onerror = function(event) {
        document.getElementById("status").innerHTML = "음성 인식 에러: " + event.error;
        if (event.error === 'not-allowed') {
            alert('마이크 권한을 허용해주세요.');
        }
        stopRecognition();
    };
    
    recognition.onend = function() {
        if (isRecording) {
            recognition.start();
        }
    };
    
    try {
        recognition.start();
    } catch (err) {
        console.error('음성 인식 시작 오류:', err);
        alert('음성 인식을 시작할 수 없습니다. HTTPS 연결을 확인해주세요.');
    }
}

function stopRecognition() {
    if (recognition) {
        recognition.stop();
        isRecording = false;
        document.getElementById("status").innerHTML = "음성 인식 대기 중...";
        document.getElementById("voiceButton").innerHTML = "음성 인식 시작";
        document.getElementById("voiceButton").classList.remove("recording");
    }
}
</script>

<style>
.recording {
    background-color: red;
    color: white;
}
button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    margin-bottom: 10px;
}
</style>

<button id="voiceButton" onclick="toggleRecognition()">음성 인식 시작</button>
<p id="status">음성 인식 대기 중...</p>
<p id="result"></p>
"""

def main():
    st.title("음성 대화 챗봇")
    
    # 음성 인식 컴포넌트 추가
    st.components.v1.html(html_code, height=200)
    
    # 세션 상태 처리
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # 음성 인식 결과 처리
    if "user_input" in st.session_state:
        user_input = st.session_state.user_input
        chatbot_response = get_chatbot_response(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": chatbot_response})
    
    # 대화 기록 표시
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.text(f"사용자: {message['content']}")
        else:
            st.text(message["content"])

if __name__ == "__main__":
    main()
