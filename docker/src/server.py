import subprocess

from flask import Flask
from flask import request
from flask import send_file
from github import GitHub
from graphviz import Graphviz

app = Flask(__name__)

@app.route('/health')
def health():
    return 'Healthy'

@app.route('/generate_image')
def generate_image():
    repo = request.args.get('repository')
    filepath = request.args.get('filepath')

    try:
        # Pull the file from GitHub
        dot_file = GitHub.download_file(repo, filepath)

        # Generate Graphviz image from dot file
        png_file = Graphviz.generate_png(dot_file)

    # TOOD: catch more meaningful exception and log
    except Exception:
        return send_file('static/404.png', mimetype='image/png')

    return send_file(png_file, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
