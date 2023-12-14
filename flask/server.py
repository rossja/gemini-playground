#!/usr/bin/env python
import os
import requests

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
# def hello():
# 	return "Hello World!"
def testGemini():
    jsonData = {
        "prompt": {
            "text": "Write a story about a magical flying bison"
        }
    }
    requrl = os.environ.get("GEMINI_API_URL") + "?key=" + os.environ.get("GEMINI_API_KEY")
    r = requests.post(requrl, json=jsonData)
    jsonResponse = r.json()
    # jsonResponse = {'candidates': [{'output': "Once upon a time, there was a magical flying bison named Appa. He lived in the Earth Kingdom with his friends Aang, Katara, Sokka, and Toph. Appa was a loyal and kind friend, and he always helped his friends when they needed him.\n\nOne day, Aang, Katara, Sokka, and Toph were on a journey to the North Pole. They were attacked by a group of Fire Nation soldiers, and Appa was captured. Aang and his friends were heartbroken, and they didn't know what to do.\n\nAang decided to go on a quest to find Appa. He traveled all over the world, searching for his friend. He faced many challenges along the way, but he never gave up hope.\n\nFinally, Aang found Appa in a Fire Nation camp. He was being held prisoner, and he was very weak. Aang freed Appa, and they escaped together.\n\nAang and Appa were reunited, and they were so happy to see each other. They hugged each other tightly, and they flew back to their friends.\n\nAang and his friends were so happy to have Appa back. They knew that they could always count on him to help them out.\n\nAppa was a loyal and kind friend, and he was always there for his friends. He was a true friend, and they were lucky to have him.", 'safetyRatings': [{'category': 'HARM_CATEGORY_DEROGATORY', 'probability': 'NEGLIGIBLE'}, {'category': 'HARM_CATEGORY_TOXICITY', 'probability': 'NEGLIGIBLE'}, {'category': 'HARM_CATEGORY_VIOLENCE', 'probability': 'NEGLIGIBLE'}, {'category': 'HARM_CATEGORY_SEXUAL', 'probability': 'NEGLIGIBLE'}, {'category': 'HARM_CATEGORY_MEDICAL', 'probability': 'NEGLIGIBLE'}, {'category': 'HARM_CATEGORY_DANGEROUS', 'probability': 'NEGLIGIBLE'}]}]}
    # print(r.status_code)
    # print(r.json())
    output = jsonResponse["candidates"][0]["output"]
    return render_template('index.html', output=output, prompt=jsonData["prompt"]["text"])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9001), debug=os.environ.get("FLASK_DEBUG", True))