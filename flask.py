from flask import Flask, request
from flask.ext.cors import CORS
import urllib

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET','POST'])
def hello():
    #url = "http://www.imdb.com/title/tt0109830/soundtrack"
    if request.method == 'POST':
        data = str(request.form['link'])
        url = data
        print(url)
    html_data = urllib.urlopen(url).read()

    print html_data