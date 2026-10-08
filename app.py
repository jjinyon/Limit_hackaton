import streamlit as st

st.title("이판사판")

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
