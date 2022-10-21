#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL

"""

if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        rep = response.read()
        print(rep.read().decode('utf-8'))
