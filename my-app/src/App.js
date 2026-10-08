import React from 'react';
import MultiTextInput from './components/MultiTextInput';

function App() {
  const handleTextSubmit = (combinedText) => {
    console.log("Combined Text:", combinedText); // 결합된 텍스트 콘솔 출력
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>두 개의 입력창 예제</p>
        <MultiTextInput onSubmit={handleTextSubmit} />
      </header>
    </div>
  );
}

export default App;