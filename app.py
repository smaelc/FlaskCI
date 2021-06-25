# coding: utf-8

from flask import render_template
from .settings import app

@app.route('/', methods=('GET',))
def index():
    name = 'Smael'
    return render_template('book/index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
