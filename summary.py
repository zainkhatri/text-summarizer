from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__, template_folder='templates')  # Assuming your HTML file is in the 'templates' folder
CORS(app)

# Load a smaller summarization model using Hugging Face Transformers
summarizer = pipeline("summarization", model="facebook/bart-base")

# Define the home endpoint to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Define the summarize endpoint
@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        input_text = data.get('text')

        if not input_text:
            return jsonify({'error': 'No text provided for summarization'}), 400

        summary_text = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        return jsonify({'summary': summary_text[0]['summary_text']})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)