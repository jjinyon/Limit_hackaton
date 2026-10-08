import streamlit as st
import api

st.title("진단")

if 'str_1' in st.session_state and 'str_2' in st.session_state:
    val1 = st.session_state['str_1']
    val2 = st.session_state['str_2']
    result= api.processData(val1, val2)
    
    st.write("문제점:")
    st.json(result)


else:
    st.error("입력된 이야기가 없습니다. 메인 페이지에서 다시 진행해주세요.")
if st.button("처음으로 돌아가기"):
    st.session_state.clear()
    st.switch_page("main.py")
