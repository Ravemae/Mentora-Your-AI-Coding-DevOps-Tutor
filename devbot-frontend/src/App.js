import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    setMessages([...messages, { sender: 'user', text: input }]);
    setInput('');

    try {
      const response = await axios.post('http://localhost:8000/chat', {
        user_input: input,
      });

      setMessages((prev) => [
        ...prev,
        { sender: 'bot', text: response.data.response },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { sender: 'bot', text: 'Error communicating with server.' },
      ]);
    }
  };

  return (
    <div className="chat-container">
      <h1>DevBot AI Chat</h1>
      <div className="chat-box">
        {messages.map((msg, idx) => (
          <div key={idx} className={`chat-message ${msg.sender}`}>
            <b>{msg.sender === 'user' ? 'You' : 'DevBot'}:</b> {msg.text}
          </div>
        ))}
      </div>
      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask me about Python, Git, or Docker..."
          onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
