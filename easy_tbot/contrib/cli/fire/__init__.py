"""This module contain a cli backend base on fire"""
try:
    import fire
    # assert fire.__version__ >= 0.4
except:
    print("Warning: Code in `easy_tbot.contrib.cli.fire` requires `fire>=0.4`.")
    print("FIX: You can install it with `pip install easy_tbot[fire]`.")
    raise

from ._backend import FireBackend