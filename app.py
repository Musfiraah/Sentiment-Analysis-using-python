
from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']

        # Load sentiment analysis pipeline
        sentiment_analyzer = pipeline('sentiment-analysis')

        # Get sentiment prediction
        result = sentiment_analyzer(text)

        # Extract predicted label
        label = result[0]['label']


        return render_template('result.html', text=text, label=label)

if __name__ == '__main__':
    app.run(debug=True)