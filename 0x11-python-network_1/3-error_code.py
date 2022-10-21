#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response
"""

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from sys import argv

    request = Request(argv[1])
    try:
        with urlopen(request) as response:
            rep = response.read()
            print(rep.decode('utf-8'))
    except HTTPError as err:
        print('Error code:', e.code)
