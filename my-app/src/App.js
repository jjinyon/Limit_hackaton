import React, { useState } from 'react';
import MultiTextInput from './components/MultiTextInput';
import axios from 'axios';
import { REACT_APP_API_ENDPOINT, REACT_APP_ACCESS_TOKEN } from './config';

function App() {
  const [maleSide, setMaleSide] = useState('');
  const [femaleSide, setFemaleSide] = useState('');

  const handleMaleChange = (value) => {
    setMaleSide(value);
  };

  const handleFemaleChange = (value) => {
    setFemaleSide(value);
  };

  const handleSubmit = async () => {
    try {
      // HyperCLOVA API 호출을 위한 데이터 준비
      const clovaRequestPayload = {
        messages: [
          {
            role: 'system',
            content: [
              {
                type: 'text',
                text: `현재 두 연인의 관계개선 상담을 하고 있습니다. 맥락은 다음과 같습니다.\n남성측 : ${maleSide}\n여성측 :${femaleSide}`
              }
            ]
          },
          {
            role: 'assistant',
            content: [] // 여기에 어시스턴트 메시지 객체를 추가할 수 있습니다.
          }
        ],
        temperature: 0.5, // 온도 설정
        max_tokens: 1024, // 최대 토큰 수
        top_k: 40, // 상위 K개 선택
        frequency_penalty: 0.0, // 빈도 페널티
        presence_penalty: 0.0 // 존재 페널티
      };

      // API 호출 (axios 사용 예시)
      const response = await axios.post(REACT_APP_API_ENDPOINT, clovaRequestPayload, {
        headers: {
          Authorization: `Bearer ${REACT_APP_ACCESS_TOKEN}`,
          'X-NCP-CLOVASTUDIO-REQUEST-ID': Math.random().toString()
        }
      });

      console.log('Response from HyperCLOVA:', response.data);
      alert('API 호출 성공!');
    } catch (error) {
      console.error('Error calling HyperCLOVA API:', error);
      alert('API 호출 실패!');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>연애 상담 챗봇</h1>
        <div>
          <h2>남자측 입장:</h2>
          <MultiTextInput 
            initialValue={maleSide}
            onChangeText={setMaleSide}
          />
          <h2>여자측 입장:</h2>
          <MultiTextInput 
            initialValue={femaleSide}
            onChangeText={setFemaleSide}
          />
        </div>
        <button onClick={handleSubmit}>상담 요청</button>
      </header>
    </div>
  );
}

export default App;