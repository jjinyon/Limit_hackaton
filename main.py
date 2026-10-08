# main.py
import streamlit as st
import api  # api.py에서 함수 가져오기

st.title("초간단 파이썬 웹 앱")

# 사용자로부터 스트링 두 개 입력받기
input_1 = st.text_input("남자의 입장을 입력하세요:")
input_2 = st.text_input("여자의 입장를 입력하세요:")

# 버튼을 누르면 실행
if st.button("실행하기"):
    if input_1 and input_2:
        # api.py의 함수로 값 전달 후 딕셔너리 반환받기
        api.male_side = input_1
        api.female_side = input_2
        
        # 반환받은 딕셔너리를 화면에 출력
        st.write("결과:")
        st.json(api.data)
    else:
        st.warning("두 칸을 모두 입력해주세요.")