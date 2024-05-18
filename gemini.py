from flask import Flask, request, Response
import spacy
from spacy import displacy
import google.generativeai as genai
import json
from news import *

# flask initialize
app = Flask(__name__)

# api keys
file = open('keys.json')
keys = json.load(file)

# genai
genai.configure(api_key=keys['gemini'])
model = genai.GenerativeModel('gemini-pro')

# spaCy
NER = spacy.load("en_core_web_lg")
ruler = NER.add_pipe("entity_ruler", before="ner")
exclude = [
    {"label": "NOT_PERSON", "pattern": [{"LOWER": "jpg"}]},
    {"label": "NOT_PERSON", "pattern": [{"LOWER": "png"}]},
    {"label": "NOT_PERSON", "pattern": [{"TEXT": {"REGEX": ".*-.*"}}]}
]

ruler.add_patterns(exclude)

@app.route('/', methods=['GET', 'POST'])
def generate_story():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            article = get_content(url)
            return article
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