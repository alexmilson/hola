import React, { useState } from "react";

function SymptomChecker() {
  const [symptoms, setSymptoms] = useState("");
  const [result, setResult] = useState("");

  const checkSymptoms = async () => {
    const response = await fetch(`https://your-api.onrender.com/symptom_checker?symptoms=${symptoms}`);
    const data = await response.json();
    setResult(data.possible_diseases ? data.possible_diseases.join(", ") : data.message);
  };

  return (
    <div>
      <input value={symptoms} onChange={(e) => setSymptoms(e.target.value)} placeholder="Enter symptoms (e.g. fever, cough)" />
      <button onClick={checkSymptoms}>Check Symptoms</button>
      <p>{result}</p>
    </div>
  );
}

export default SymptomChecker;

