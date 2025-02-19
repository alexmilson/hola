from fastapi import FastAPI
from model import get_answer
from symptom_checker import check_symptoms

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Healthcare Chatbot API is running"}

@app.get("/ask")
def ask_question(question: str):
    answer = get_answer(question)
    return {"answer": answer}

@app.get("/symptom_checker")
def symptom_checker(symptoms: str):
    symptoms_list = symptoms.split(", ")
    diseases = check_symptoms(symptoms_list)
    return {"possible_diseases": diseases}

