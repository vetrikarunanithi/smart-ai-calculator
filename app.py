from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Google Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/')
def home():
    return jsonify({
        'message': 'Smart AI Calculator API (Gemini)',
        'use': 'POST /calculate or /explain'
    })

# ---------- BASIC CALCULATOR ----------
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression', '')

        if not expression:
            return jsonify({'error': 'No expression provided!'}), 400

        # Replace × and ÷ symbols
        expression = expression.replace('×', '*').replace('÷', '/')

        # Allow only safe math characters
        for ch in expression:
            if ch not in "0123456789+-*/.%() ":
                return jsonify({'error': 'Invalid character found!'}), 400

        try:
            result = eval(expression)
        except ZeroDivisionError:
            return jsonify({'error': 'Cannot divide by zero!'}), 400
        except Exception:
            return jsonify({'error': 'Invalid expression!'}), 400

        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ---------- AI EXPLANATION (GEMINI) ----------
@app.route('/explain', methods=['POST'])
def explain():
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        if not expression:
            return jsonify({'error': 'No expression provided!'}), 400

        prompt = (
            f"Explain step-by-step how to solve this math expression: {expression}. "
            f"Write it in a clear, structured, and easy-to-read markdown format with headings, bold text, and bullet points."
        )

        # Use Gemini model
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)

        explanation = response.text.strip()
        return jsonify({'explanation': explanation}), 200
    except Exception as e:
        return jsonify({'error': f'AI error: {str(e)}'}), 500


# ---------- HEALTH CHECK ----------
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
