from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/form_shit/', methods=['POST'])
def handle_data():
   projectpath = request.form.input_ticker
   #your code
