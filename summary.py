from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

# Load a smaller summarization model using Hugging Face Transformers
summarizer = pipeline("summarization", model="facebook/bart-base")

# Define the home endpoint
@app.route('/')
def home():
    return "Welcome to the Text Summarizer API. Use the /summarize endpoint to summarize text."

# Define the summarize endpoint
@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        # Get the input text from the POST request
        data = request.get_json()
        input_text = data.get('text')

        # Return an error if no text is provided
        if not input_text:
            return jsonify({'error': 'No text provided for summarization'}), 400

        # Generate the summary using the smaller BART model
        summary_text = summarizer(input_text, max_length=130, min_length=30, do_sample=False)

        # Return the summary in JSON format
        return jsonify({'summary': summary_text[0]['summary_text']})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app (for local testing purposes)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
