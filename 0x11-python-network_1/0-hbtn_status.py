#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as site:
        rep = site.read()
        print('Body response:')
        print('\t- type: {}'.format(type(rep)))
        print('\t- content: {}'.format(rep))
        print('\t- utf8 content: {}'.format(rep.decode('utf-8')))
