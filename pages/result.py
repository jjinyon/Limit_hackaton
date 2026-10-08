import streamlit as st
import api
import json

st.set_page_config(page_title="#이판사판", layout="centered")
st.markdown(
    """
    <style>
    /* 전체 앱 배경 설정 */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }

    /* 메인 콘텐츠 영역을 투명하거나 보기 좋게 조정 */
    .block-container {
        background-color: rgba(255, 255, 255, 0.6); /* 반투명 흰색 배경으로 가독성 확보 */
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px); /* 배경 흐림 효과 */
    }

    /* 그라데이션이 움직이는 애니메이션 정의 */
    @keyframes gradient {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
    st.write("##### ⚠️문제점:")
    st.write("###### " + problem)
    st.write("\n")
    st.write("##### 💡해결방법:")
    st.write("###### "+solution)
    st.write("\n")
    if(val3): #남자
        maleFeelings = result["maleFeelings"]
        st.write("##### 👨남자가 느낀 점:")
        st.write("###### "+ maleFeelings)
        st.write("\n")
    if(val4): #여자
        femaleFeelings = result["femaleFeelings"]
        st.write("##### 👩여자가 느낀 점:")
        st.write("###### "+ femaleFeelings)
        st.write("\n")
    if(val5): #타임라인
        recap = result["recap"]
        st.write("##### 🕑타임라인:")
        st.write(recap)
        st.write("\n")
    if(val6): #과실비율
        ratio = result["ratio"]
        st.write("##### ⚖️AI가 생각한 과실비율:")
        st.write("### " + "  " + ratio)

    
    
else:
    st.error("입력된 이야기가 없습니다. 메인 페이지에서 다시 진행해주세요.")

if st.button("처음으로 돌아가기"):
    st.session_state.clear()
    st.switch_page("app.py")
