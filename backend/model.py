from transformers import pipeline

# Load medical Q&A model from Hugging Face
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def get_answer(question):
    context = """
    The flu is a viral infection that affects the respiratory system. Symptoms include fever, cough, sore throat, body aches, and fatigue. 
    COVID-19 is a disease caused by the SARS-CoV-2 virus. It has symptoms similar to the flu but can also include loss of taste and smell.
    """
    result = qa_pipeline(question=question, context=context)
    return result["answer"]

