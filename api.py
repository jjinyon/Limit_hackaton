import requests
import os
import uuid
from dotenv import load_dotenv

load_dotenv(override=True)

model = "HCX-007"
URL = f"https://limitai.43.202.27.129.sslip.io/v3/chat-completions/{model}"
ClovaKey = os.getenv("ClovaKey")

headers = {
    "Authorization": f"Bearer {ClovaKey}",
    "X-NCP-CLOVASTUDIO-REQUEST-ID": str(uuid.uuid4()),
    "Content-Type": "application/json",
    "Accept": "application/json",
}

male_side = ""
female_side = ""
context = "당신은 능력있는 커플심리상담가입니다. 현재 두 연인의 관계개선 상담을 하고 있습니다."
#주의사항
#1. 남자측 입장과 여자측 입자은 서로를 향한 편견과 오해가 있을 수 있음을 명심합니다.
#2. 남자측 입장과 여자측 입장을 서로에게 그대로 공개하여 양측이 상처를 입지 않도록 합니다.
prompt = f"맥락은 다음과 같습니다. 남성측 : {male_side} / 여성측 : {female_side}."

payload = {
    "messages": [
        {"role": "system", 
         "content": [{"type": "text", 
                      "text": context}]}, # AI 역할
        {"role": "user", 
         "content": [{"type": "text", "text": prompt}]}, # 입력
    ],
    "thinking": {"effort": "medium"}, #추론 정도 low / medium / high
    "topP": 0.8,
    "topK": 0,
    "temperature": 0.5,
    "repetitionPenalty": 1.1,
}

resp = requests.post(URL, headers=headers, json=payload, timeout=60)

if resp.status_code != 200:
    print("Error!")

data = resp.json()
print(data)