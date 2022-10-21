#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    username = sys.argv[1]
    password = sys.argv[2]

    basic = HTTPBasicAuth(username, password)
    r = requests.get('https://api.github.com/user', auth=basic)
    print(r.json().get('id'))
