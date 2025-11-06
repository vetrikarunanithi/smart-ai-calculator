from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)  # allows frontend (HTML/JS) to talk to backend

@app.route('/')
def home():
    return jsonify({
        'message': 'Calculator API is running',
        'use': 'Send POST request'
    })

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # get data from frontend
        data = request.get_json()
        expression = data.get('expression', '')

        if not expression:
            return jsonify({'error': 'No expression provided!'}), 400

        # replace symbols if needed
        expression = expression.replace('×', '*').replace('÷', '/')

        # basic safety check (only numbers and math symbols)
        for ch in expression:
            if ch not in "0123456789+-*/.%() ":
                return jsonify({'error': 'Invalid character found!'}), 400

        # do the math
        try:
            result = eval(expression)
        except ZeroDivisionError:
            return jsonify({'error': 'Cannot divide by zero!'}), 400
        except Exception:
            return jsonify({'error': 'Invalid!'}), 400

        return jsonify({'result': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Initialize AI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/explain', methods=['POST'])
def explain():
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        if not expression:
            return jsonify({'error': 'No expression provided!'}), 400

        # Generate explanation using GPT model
        prompt = f"Explain step-by-step how to solve this math expression: {expression}"

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful math tutor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        explanation = response.choices[0].message.content.strip()
        return jsonify({'explanation': explanation}), 200

    except Exception as e:
        return jsonify({'error': f'AI error: {str(e)}'}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
