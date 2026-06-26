from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

api_key = os.environ.get('GOOGLE_API_KEY') or os.environ.get('AXION_API_KEY') or 'AQ.Ab8RN6KkaeaXVcilHhHcifnMVRX2nUNdWGYoElKiDkUoJpuxWA'
# Use a supported Gemini model for google.generativeai / GenAI calls.
DEFAULT_MODEL = 'models/gemini-2.5-flash'
raw_model_name = os.environ.get('AI_MODEL', DEFAULT_MODEL)
model_name = raw_model_name if raw_model_name.startswith('models/') else f'models/{raw_model_name}'
try:
    import google.generativeai as genai
    if api_key:
        genai.configure(api_key=api_key)
except ImportError:
    genai = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(force=True)
    message = data.get('message', '').strip()
    if not message:
        return jsonify({'reply': 'Please type a request.'})
    if not api_key or genai is None:
        return jsonify({'reply': 'Set GOOGLE_API_KEY or AXION_API_KEY and install google-generativeai.'})
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(message)
        return jsonify({'reply': response.text})
    except Exception as error:
        error_text = str(error)
        if model_name != DEFAULT_MODEL and ('404' in error_text or 'not supported' in error_text or 'generateContent' in error_text):
            try:
                fallback_model = DEFAULT_MODEL
                fallback = genai.GenerativeModel(fallback_model)
                response = fallback.generate_content(message)
                return jsonify({'reply': f"{response.text}\n\n(Note: Fell back to {fallback_model} because {model_name} is unavailable.)"})
            except Exception as fallback_error:
                return jsonify({'reply': f'AI error: {error_text}; fallback error: {fallback_error}'})
        return jsonify({'reply': f'AI error: {error_text}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))