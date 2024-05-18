from flask import Flask, request, Response
from newsplease import NewsPlease
import spacy
from spacy import displacy
import google.generativeai as genai
import json

# flask initialize
app = Flask(__name__)

# api keys
file = open('keys.json')
keys = json.load(file)

# genai
genai.configure(api_key=keys['gemini'])
model = genai.GenerativeModel('gemini-pro')

@app.route('/', methods=['GET', 'POST'])
def generate_story():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            article = NewsPlease.from_url(url)
            return article.authors
        else:
            return "Please provide a valid URL."
    else:
        return """
        <form method="post">
            <label for="url">Enter the URL:</label><br>
            <input type="text" id="url" name="url"><br>
            <input type="submit" value="Submit">
        </form>
        """

if __name__ == '__main__':
    app.run(debug=True)