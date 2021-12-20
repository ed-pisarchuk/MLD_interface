from flask import Flask, render_template, request

import os
from model import process_image

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    imagefile = request.files.get('image')
    full_name = os.path.join(os.getcwd(), 'files', imagefile.filename)
    imagefile.save(full_name)
    [classname, img_name] = process_image(full_name)
    return render_template('answer.html', classname=classname, img_name='/mo_classes/' + img_name)

if __name__ == "__main__":
    app.run(debug=True)