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
