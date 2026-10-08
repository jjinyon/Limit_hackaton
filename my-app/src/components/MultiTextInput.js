import React, { useState } from 'react';

const MultiTextInput = ({ onSubmit }) => {
  const [texts, setTexts] = useState([ '', '' ]); // 초기 상태 설정

  const handleChange = (index, value) => {
    setTexts(prevState => {
      const newValues = [...prevState];
      newValues[index] = value;
      return newValues;
    });
  };

  const handleSubmit = () => {
    const combinedText = texts.join(', ');
    onSubmit(combinedText);

    // 제출 후 입력창 비우기
    setTexts(['', '']);
  };

  return (
    <div>
      <div>
        <input 
          type="text" 
          value={texts[0]} 
          onChange={(e) => handleChange(0, e.target.value)}
        />
        <input 
          type="text" 
          value={texts[1]} 
          onChange={(e) => handleChange(1, e.target.value)}
        />
      </div>
      <button onClick={handleSubmit}>제출</button>
    </div>
  );
};

export default MultiTextInput;