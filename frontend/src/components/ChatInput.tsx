import React, { useState } from 'react';

const ChatInput: React.FC = () => {
  const [value, setValue] = useState('');

  const handleSend = () => {
    if (value.trim()) {
      // Send message logic here
      setValue('');
    }
  };

  return (
    <div className="flex p-4 bg-white border-t">
      <input
        className="flex-1 border rounded-l px-3 py-2 focus:outline-none"
        type="text"
        placeholder="Type your message..."
        value={value}
        onChange={e => setValue(e.target.value)}
        onKeyDown={e => e.key === 'Enter' && handleSend()}
      />
      <button
        className="bg-blue-500 text-white px-4 py-2 rounded-r hover:bg-blue-600"
        onClick={handleSend}
      >
        Send
      </button>
    </div>
  );
};

export default ChatInput; 