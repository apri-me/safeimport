from contextlib import contextmanager


@contextmanager
def safe_import(depth: int):
    """When your base is <depth> times outer your script (depth >= 1)"""
    if type(depth) != type(0) or depth < 1:
        raise Exception("Depth should be integer and greater than zero!")
    try:
        import os
        import sys
        ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "/".join([".."] * (depth + 1))))
        sys.path.append(ROOT_DIR)
        yield 
    finally:
        del ROOT_DIR, os, sys
