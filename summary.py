from flask import Flask, render_template, request
from transformers import BartForConditionalGeneration, BartTokenizer
# Initialize the Flask app
app = Flask(__name__)
# Load the BART model and tokenizer
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    if request.method == "POST":
        # Get the user input text
        user_input = request.form["text"]
        
        # Tokenize input text and generate summary with more descriptive parameters
        inputs = tokenizer.encode("summarize: " + user_input, return_tensors="pt", max_length=1024, truncation=True)
        
        # Adjust the parameters to produce more descriptive summaries
        summary_ids = model.generate(
            inputs,
            max_length=300,  # Increased max length for more detail
            min_length=100,  # Increased min length to ensure a detailed summary
            length_penalty=1.2,  # Slightly reduced length penalty for longer outputs
            num_beams=6,  # More beams for better output quality
            early_stopping=True
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    # Render the HTML template and pass the summary to the frontend
    return render_template("index.html", summary=summary)
if __name__ == "__main__":
    app.run(debug=True)