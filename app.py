import streamlit as st

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

col1, col2 = st.columns([3, 1])
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
        
