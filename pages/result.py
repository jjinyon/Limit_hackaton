import streamlit as st
import api
import json

col1, col2 = st.columns([1, 2])
with col1:
    st.title("진단")
    
with col2:
    st.image("char.png", caption="")


if 'str_1' in st.session_state and 'str_2' in st.session_state:
    val1 = st.session_state['str_1']
    val2 = st.session_state['str_2']
    val3 = st.session_state['bool_1']
    val4 = st.session_state['bool_2']
    val5 = st.session_state['bool_3']
    val6 = st.session_state['bool_4']
    result= json.loads(api.processData(val1, val2, val3, val4, val5, val6))


    problem = result["problem"]
    solution = result["solution"]
    st.write("##### 문제점:")
    st.write("###### " + problem)
    st.write("##### 해결방법:")
    st.write("###### "+solution)
    if(val3): #남자
        maleFeelings = result["maleFeelings"]
        st.write("##### 남자가 느낀 점:")
        st.write("###### "+ maleFeelings)
    if(val4): #여자
        femaleFeelings = result["femaleFeelings"]
        st.write("##### 여자가 느낀 점:")
        st.write("###### "+ femaleFeelings)
    if(val5): #타임라인
        recap = result["recap"]
        st.write("##### 타임라인:")
        st.write(recap)
    if(val6): #과실비율
        ratio = result["ratio"]
        st.write("##### AI가 생각한 과실비율:")
        st.write("####### "+ ratio)

    
    
else:
    st.error("입력된 이야기가 없습니다. 메인 페이지에서 다시 진행해주세요.")

if st.button("처음으로 돌아가기"):
    st.session_state.clear()
    st.switch_page("app.py")
