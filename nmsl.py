# -*- coding:utf-8 -*-

from flask import Flask, render_template, jsonify, request
from nmsl_local import text_to_emoji
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/process',methods= ['POST'])
def process():
    # text = request.form['firstname']
    # output = text_to_emoji(text)

    output = text_to_emoji(request.form['text'], method=int(request.form['method']))
    print(request.form['method'])
    if output:
        return jsonify({'output': output})
    else:
        return jsonify({'error' : 'Missing data!'})
if __name__ == '__main__':
    app.debug = True
    app.run(host='172.21.0.13', port=8000)