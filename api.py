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

context = "당신은 능력있는 커플심리상담가입니다. 현재 두 연인의 관계개선 상담을 하고 있습니다. 맥락은 다음과 같습니다."
prompt = ""

payload = {
    "messages": [
        {"role": "system", 
         "content": [{"type": "text", 
                      "text": role}]}, # AI 역할
        {"role": "user", 
         "content": [{"type": "text", "text": response}]}, # 입력
    ],
    "thinking": {"effort": "medium"},
    "topP": 0.8,
    "topK": 0,
    "temperature": 0.5,
    "repetitionPenalty": 1.1,
}

resp = requests.post(URL, headers=headers, json=payload, timeout=60)

data = resp.json()
print(data)