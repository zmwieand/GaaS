import hashlib
import os
import requests

class GitHub():
    """
    Class to pull files from GitHub repositories.
    """

    def download_file(repository, filepath):
        """
        Function to download a file from a git repository
        """
        url = f"https://api.github.com/repos/{repository}/contents/{filepath}"
        auth_token = os.getenv('GIT_TOKEN')
        headers = {
            "Authorization": f"token {auth_token}",
            "Accept": "application/vnd.github.v3.raw"
        }

        resp = requests.get(url, headers=headers)

        if resp.status_code != 200:
            raise GitHubFileDownloadException()

        # Filename will be saved to<sha256(file)>.dot
        data = resp.content
        dot_file = hashlib.sha256(data).hexdigest() + ".dot"
        with open(dot_file, 'w') as f:
            f.write(data.decode('utf-8'))

        return dot_file

class GitHubFileDownloadException(Exception):
    """
    Exception thrown on a failed file download from GitHub.
    """
    pass
