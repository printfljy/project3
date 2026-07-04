import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="가위바위보 게임",
    page_icon="✌️",
    layout="centered"
)

# CSS 스타일
st.markdown("""
<style>
.stApp {
    background-color: #90EE90;
    color: black;
}

h1, h2, h3, h4, h5, h6, p, div, span, label {
    color: black !important;
}

.stButton > button {
    background-color: white;
    color: black !important;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    width: 100%;
    height: 50px;
}
</style>
""", unsafe_allow_html=True)

# 상태 저장
if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "computer" not in st.session_state:
    st.session_state.computer = ""

if "result" not in st.session_state:
    st.session_state.result = ""

# 승패 판정 함수
def judge(user, computer):
    if user == computer:
        return "🤝 비겼습니다!"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        return "🎉 당신이 이겼습니다!"
    else:
        return "😢 당신이 졌습니다."

# 메인 화면
if not st.session_state.game_over:

    st.markdown(
        "<h1 style='text-align:center;'>✌️✊✋ 가위, 바위, 보!</h1>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("### 하나를 선택하세요!")

    col1, col2, col3 = st.columns(3)

    choices = ["가위", "바위", "보"]

    if col1.button("✌️ 가위"):
        user = "가위"
    elif col2.button("✊ 바위"):
        user = "바위"
    elif col3.button("✋ 보"):
        user = "보"
    else:
        user = None

    if user:
        computer = random.choice(choices)

        st.session_state.computer = computer
        st.session_state.result = judge(user, computer)
        st.session_state.game_over = True

        st.rerun()

# 결과 화면
else:

    st.markdown(
        "<h1 style='text-align:center;'>🎮 결과</h1>",
        unsafe_allow_html=True
    )

    st.write("")
    st.markdown(f"### 컴퓨터는 **{st.session_state.computer}**를 선택했습니다!")
    st.write("")
    st.markdown(f"## {st.session_state.result}")

    st.write("")
    st.write("")

    if st.button("🔄 다시하기"):
        st.session_state.game_over = False
        st.session_state.computer = ""
        st.session_state.result = ""
        st.rerun()
