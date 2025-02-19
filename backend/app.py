from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the DialoGPT-medium-med model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium-med")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium-med")

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('message', '')

        # Generate response
        input_ids = tokenizer.encode(
            user_input + tokenizer.eos_token, 
            return_tensors='pt'
        )
        output = model.generate(
            input_ids,
            max_length=200,
            pad_token_id=tokenizer.eos_token_id,
            temperature=0.7,
            top_k=50
        )
        response = tokenizer.decode(
            output[:, input_ids.shape[-1]:][0], 
            skip_special_tokens=True
        )

        return jsonify({'response': response})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
