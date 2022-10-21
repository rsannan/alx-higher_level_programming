#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the X-Request-Id variable
found in the header of the response
"""
if __name__ == "__main__":
    import sys
    import urllib.request

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        rep = response.info()
        print(rep.get('X-Request-Id'))
