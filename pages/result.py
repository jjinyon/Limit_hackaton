import streamlit as st
import api
import json

st.title("진단")

if 'str_1' in st.session_state and 'str_2' in st.session_state:
    val1 = st.session_state['str_1']
    val2 = st.session_state['str_2']
    result= json.loads(api.processData(val1, val2))
    problem = result["problem"]
    femaleFeelings = result["femaleFeelings"]
    maleFeelings = result["maleFeelings"]
    solution = result["solution"]
    recap = result["recap"]

    st.write("문제점:")
    st.markdown("**"+problem+"**")
    st.write("타임라인:")
    st.write(recap)
    st.write("남자가 느낀 점:")
    st.write(maleFeelings)
    st.write("여자가 느낀 점:")
    st.write(femaleFeelings)
    st.write("해결방법:")
    st.write(solution)
    
else:
    st.error("입력된 이야기가 없습니다. 메인 페이지에서 다시 진행해주세요.")

if st.button("처음으로 돌아가기"):
    st.session_state.clear()
    st.switch_page("app.py")
