from lib2to3.fixes.fix_input import context

from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import generativeai as genai
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    context = 'Responda como se fosse uma pessoa super inteligente'
    prompt = request.args.get('prompt')
    input_ia = f'{context}: {prompt}'
    output = model.generate_content(input_ia)
    return {'message': output.text}

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASH_DEBUG'))