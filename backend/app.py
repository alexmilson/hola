from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the BioGPT-Large model using pipeline
pipe = pipeline("text-generation", model="microsoft/BioGPT-Large")

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('message', '')

        # Generate response using the pipeline
        response = pipe(
            user_input,
            max_length=200,
            temperature=0.7,
            top_k=50,
            do_sample=True,
            pad_token_id=pipe.tokenizer.eos_token_id
        )[0]['generated_text']

        return jsonify({'response': response})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
