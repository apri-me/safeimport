from contextlib import contextmanager


@contextmanager
def safe_import(depth: int, file_path: str):
    """When your base is <depth> times outer your script (depth >= 0)
    file_abs_path can be achieved from __file__ variable"""
    if type(depth) != type(0) or depth < 1:
        raise Exception("Depth should be integer and greater than or equal to zero!")
    try:
        import os
        import sys
        print(__file__)
        ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(file_path), "/".join([".."] * (depth))))
        sys.path.append(ROOT_DIR)
        yield 
    finally:
        del ROOT_DIR, os, sys

