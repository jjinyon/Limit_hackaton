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

male_side = "여친한테 빰을 맞았습니다"
female_side = "남자친구가 너무 멍청합니다"
context = "당신은 능력있는 커플심리상담가입니다. 현재 두 연인의 관계개선 상담을 하고 있습니다. 미리 정의한 json schema에 맞춰 응답합니다. 남자측 입장과 여자측 입자은 서로를 향한 편견과 오해가 있을 수 있음을 명심합니다."

prompt = f"맥락은 다음과 같습니다. 남성측 : {male_side} / 여성측 : {female_side}."

responseStructure = {
    "type": "object",
    "properties": {
        "problem": {
            "type": "string",
            "description": "문제 명시 / 1.둘 사이에 문제가 무엇인지 묘사합니다 2.양측의 입장을 그대로 노출하지 않습니다."
        },
        "maleFeelings": {
            "type": "string",
            "description": "남자 측 감정 전달 / 1. 남자가 어떤 감정을 느끼는지 묘사합니다."
        },
        "femaleFeelings": {
            "type": "string",
            "description": "여자 측 감정 전달 / 1. 여자가 어떤 감정을 느끼는지 묘사합니다.",
        }
    },
    "required": [
        "problem",
        "maleFeelings",
        "femaleFeelings"
    ]
}

payload = {
    "messages": [
        {"role": "system", 
         "content": [{"type": "text", 
                      "text": context}]}, # AI 역할
        {"role": "user", 
         "content": [{"type": "text", "text": prompt}]}, # 입력
    ],
    "thinking": {"effort": "none"}, #추론 정도 none으로 고정
    "topP": 0.8,
    "topK": 0,
    "max_tokens": 32768,
    "temperature": 0.5,
    "repetitionPenalty": 1.1,
    "responseFormat" : {
        "type" : "json",
        "schema" : responseStructure
    }
}

resp = requests.post(URL, headers=headers, json=payload, timeout=60)

if resp.status_code != 200:
    print("Error!")

data = resp.json()
print(data)