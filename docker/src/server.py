import subprocess

from flask import Flask
from flask import request
from flask import send_file
from graphviz import Graphviz

app = Flask(__name__)

@app.route('/health')
def health():
    return 'Healthy'

@app.route('/generate_image')
def generate_image():
    repo = request.args.get('repository')
    filepath = request.args.get('filepath')

    # TODO: Pjull the file from GitHub
    # return f"{repo} -- {filepath}"
    return send_file('image.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# filepath = Graphviz.generate_image('file2.dot')
# print(filepath)
# 
# # gaas.int.acvauctions.com/get_png?repo=<>&filepath=
# def get_png():

