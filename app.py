from flask import Flask, render_template, request, redirect
from flask import request

#from bokeh.embed import components
#from bokeh.plotting import figure
#from bokeh.resources import INLINE
#from bokeh.util.string import encode_utf8

#import sys
#sys.path.append('/home/pinsley/miniconda2/pkgs/bokeh-0.12.4-py27_0/bin')
#import bokeh

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)

@app.route('/templates/form_shit/', methods=['POST', 'GET'])
def handle_data():
#    if request.method == 'POST':
    test = request.values.get('input_ticker')
#    fig = figure()
#    fig.line([1,2,3,4],[5,6,7,8])
#    js_resources = INLINE.render_js()
#    css_resources = INLINE.render_css()

#    html = flask.render_template(
#        'embed.html',
#        plot_script=script,
#        plot_div=div,
#        js_resources=js_resources,
#        css_resources=css_resources,
#    )

#    return encode_utf8(html)

    #test = request.form['input_ticker']
#   	return test
#   if request.method == 'GET':
 #       print "Hello"
   #	fucker = request.form
   # return test
   #return projectpath
   #your code
