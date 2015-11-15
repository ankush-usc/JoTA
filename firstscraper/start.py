import os

from flask import Flask, request
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET','POST'])
def whats():
    os.getcwd()

    cmd = "scrapy crawl indeed"
    """cmd = "sudo scrapy crawl whats" """
    os.system(cmd)
    return

if __name__ == "__main__":
    app.run()