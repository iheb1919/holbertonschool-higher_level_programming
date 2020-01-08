#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        x = fct(*args)
    except Exception as error:
        x = None
        print("Exception:", error, file=sys.stderr)
    return x
