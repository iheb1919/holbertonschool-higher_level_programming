#!/usr/bin/python3
"""
9-add_item
"""

if __name__ == '__main__':
    from sys import argv
    to_json_file = __import__("7-save_to_json_file").save_to_json_file
    from_json_file = __import__("8-load_from_json_file").load_from_json_file

    filename = "add_item.json"

    try:
        obj = from_json_file(filename)
    except Exception as e:
        with open(filename, 'w') as f:
            obj = []
    for i in argv[1:]:
        obj.append(i)

    to_json_file(obj, filename)
