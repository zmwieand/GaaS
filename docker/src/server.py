import subprocess

from flask import Flask
from flask import request
from flask import send_file
from github import GitHub
from github import GitHubFileDownloadException
from graphviz import Graphviz
from graphviz import GraphvizRenderException

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

    except GitHubFileDownloadException:
        app.logger.error(f'Error downloading {filepath} from {repo}')
        return send_file('static/404.png', mimetype='image/png')

    except GraphvizRenderException:
        app.logger.error(f'Error rendering {filepath} from {repo}')
        return send_file('static/404.png', mimetype='image/png')

    return send_file(png_file, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
