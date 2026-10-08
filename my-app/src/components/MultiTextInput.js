import React, { useState } from 'react';

const MultiTextInput = ({initialValue = '', onChangeText}) => {
  const [text, setText] = useState(initialValue);

  const handleChange = (event) => {
    const newText = event.target.value;
    setText(newText);
    if (onChangeText) {
      onChangeText(newText);
    }
  };

  return (
    <div>
      <textarea
        value={text}
        onChange={handleChange}
        style={{width: '100%', height: '100px'}}
      />
    </div>
  );
};

export default MultiTextInput;