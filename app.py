from flask import Flask, render_template, request
from summarizer import summarize_text
from fuzzywuzzy import fuzz
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():

    text = request.form['text']

    summary = summarize_text(text)

    similarity = fuzz.ratio(text[:100], summary)

    data = {
        "Original_Text": [text],
        "Summary": [summary],
        "Similarity": [similarity]
    }

    pd.DataFrame(data).to_csv(
        "data/history.csv",
        mode="a",
        index=False,
        header=False
    )

    return render_template(
        "index.html",
        original=text,
        summary=summary,
        similarity=similarity
    )

if __name__ == "__main__":
    app.run(debug=True)