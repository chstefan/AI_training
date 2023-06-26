from flask import Flask, render_template, request
from machinetranslation.translator import english_to_french, french_to_english

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def english_to_french_endpoint():
    english_text = request.form['text']
    french_text = english_to_french(english_text)
    return french_text

@app.route('/frenchToEnglish', methods=['POST'])
def french_to_english_endpoint():
    french_text = request.form['text']
    english_text = french_to_english(french_text)
    return english_text

if __name__ == '__main__':
    app.run()


