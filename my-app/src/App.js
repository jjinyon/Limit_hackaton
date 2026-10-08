import React from 'react';
import './App.css';
import TextInput from './components/TextInput';

function App() {
  const handleTextSubmit = (text) => {
    console.log("Parent received:", text);
    // 여기에 원하는 동작을 추가하세요. 예를 들어, 서버에 전송 등.
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <TextInput onSubmit={handleTextSubmit} />
      </header>
    </div>
  );
}

export default App;