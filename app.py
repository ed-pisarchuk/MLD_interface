from flask import Flask, render_template, request
from mo_data import mo_data_by_classes, fields_decoding

import os
from model import process_image

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/catalog')
def catalog():
    return render_template("catalog.html", catalog_data=mo_data_by_classes, fields=fields_decoding)


@app.route('/process', methods=['POST'])
def process():
    imagefile = request.files.get('image')
    full_name = os.path.join(os.getcwd(), 'static/images/user_images', imagefile.filename)
    imagefile.save(full_name)
    [current_img, predictions_cards] = process_image(full_name)
    return render_template('answer.html', user_img=current_img, predictions=predictions_cards)

if __name__ == "__main__":
    app.run(debug=True)