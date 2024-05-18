from flask import Flask, request, Response
import requests
import google.generativeai as genai
import json

app = Flask(__name__)

file = open('keys.json')
keys = json.load(file)

genai.configure(api_key=keys['gemini'])
model = genai.GenerativeModel('gemini-pro')

def get_article_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def generate_story():
    if request.method == 'POST':
        print("POST request made")
        url = request.form.get('url')
        if url:
            article_content = get_article_content(url)
            if article_content:
                prompt = "Does this following article show any bias?:" + article_content[:1000]
                response = model.generate_content(prompt)
                return Response(response.text, content_type='text/plain; charset=utf-8')
            else:
                return "Unable to fetch content from the provided URL."
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