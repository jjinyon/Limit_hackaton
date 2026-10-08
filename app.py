import streamlit as st
st.markdown(
"""
<style>
    :root {
        --primary-bg: linear-gradient(45deg, #f0f8ff, #e6f3ff);
        --text-color: #2d3436;
    }

    .stApp {

        background-image: var(--primary-bg);
        
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(255,255,255,0.3);
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        
    }
    </style>
    """,
    unsafe_allow_html=True,
)
col1, col2 = st.columns([1, 2])
with col1:
    st.title("# 이판사판")
    
with col2:
    st.image("intro.png", caption="")

# 입력창
input_1 = st.text_input("남성의 입장을 입력하세요:")
input_2 = st.text_input("여성의 입장을 입력하세요:")

# 실행 버튼
if st.button("이판사판 결과 확인"):
    if input_1 and input_2:
        # 1. 다음 페이지에서 쓸 수 있도록 session_state에 데이터 저장
        st.session_state['str_1'] = input_1
        st.session_state['str_2'] = input_2
        
        # 2. 결과 페이지로 화면 전환
        st.switch_page("pages/result.py")
    else:
        st.warning("두 칸을 모두 입력해주세요.")
        
