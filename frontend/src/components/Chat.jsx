import React, { useState } from 'react';
import axios from 'axios';
import './styles/App.css';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!inputMessage.trim()) return;

    // Add user message
    setMessages(prev => [...prev, { text: inputMessage, isBot: false }]);
    
    try {
      const response = await axios.post('http://localhost:5000/api/chat', {
        message: inputMessage
      });
      
      // Add bot response
      setMessages(prev => [...prev, { text: response.data.response, isBot: true }]);
    } catch (error) {
      setMessages(prev => [...prev, { text: "Error fetching response.", isBot: true }]);
    }
    
    setInputMessage('');
  };

  return (
    <div className="chat-container">
      <div className="chat-messages">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message ${msg.isBot ? 'bot' : 'user'}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={sendMessage} className="input-area">
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          placeholder="Ask a health-related question..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default Chat;
