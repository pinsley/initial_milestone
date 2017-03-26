from flask import Flask, render_template, request, redirect
from stockplots import make_ticker_plot

import re

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)

@app.route('/templates/form_data/', methods=['POST', 'GET'])
def handle_data():    
    
    user_input = request.values.get('input_ticker')
    
    # compulsively check for malicious injection
    pattern = r'[^a-zA-Z0-9]'
    test = re.compile(pattern).search
    validates = not(bool(test(user_input)))
    
    if validates:
        # plausible ticker, so continue
        make_ticker_plot(user_input)
        return render_template('datetime.html')
    else:
        # ticker had strange characters in it
        return 'Input ticker must consist of letters and numbers only.'