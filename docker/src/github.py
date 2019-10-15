import os
import requests

class GitHub():
    """
    Class to pull files from GitHub repositories.
    """

    def get_file(repository, filepath):
        """
        Function to download a file from a git repository
        """
        # TODO: use the github api to pull down a file
        auth_token = os.getenv('GITHUB_TOKEN')
