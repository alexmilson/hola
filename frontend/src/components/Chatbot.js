import React, { useState } from "react";

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    const response = await fetch(`https://your-api.onrender.com/ask?question=${input}`);
    const data = await response.json();
    setMessages([...messages, { text: input, user: "user" }, { text: data.answer, user: "bot" }]);
    setInput("");
  };

  return (
    <div>
      <div>
        {messages.map((msg, index) => (
          <p key={index} className={msg.user === "user" ? "user-text" : "bot-text"}>
            {msg.text}
          </p>
        ))}
      </div>
      <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Ask a health question..." />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default Chatbot;

