
import json
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Load symptom-disease data
with open("diseases.json", "r") as file:
    disease_data = json.load(file)

symptoms_list = list(disease_data.keys())

# Convert symptoms into numerical format
vectorized_symptoms = np.array([list(map(int, disease_data[symptom])) for symptom in symptoms_list])

# Train Nearest Neighbors model
knn = NearestNeighbors(n_neighbors=3, metric="euclidean")
knn.fit(vectorized_symptoms)

def check_symptoms(user_symptoms):
    user_vector = np.array([1 if symptom in user_symptoms else 0 for symptom in symptoms_list]).reshape(1, -1)
    distances, indices = knn.kneighbors(user_vector)
    
    possible_diseases = [symptoms_list[idx] for idx in indices[0]]
    return possible_diseases
