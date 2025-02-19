import React from "react";
import Chatbot from "./components/Chatbot";
import SymptomChecker from "./components/SymptomChecker";

function App() {
  return (
    <div>
      <h1>Healthcare Chatbot</h1>
      <Chatbot />
      <SymptomChecker />
    </div>
  );
}

export default App;

