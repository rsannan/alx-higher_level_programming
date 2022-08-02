#!/usr/bin/python3
"""This module adds all arguments to a Python list,
    and then saves them to a file
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Main function"""
    myfile = 'add_item.json'
    try:
        mylist = load_from_json_file(myfile)
    except FileNotFoundError:
        mylist = []
    len_args = len(sys.argv)
    for element in range(1, len_args):
        mylist.append(sys.argv[element])
    save_to_json_file(mylist, myfile)


main()
