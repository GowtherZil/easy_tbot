"""This module contains a bot backend based on aiogram"""
try:
    import aiogram
    # assert aiogram.__version__ >= 2.12
except:
    print("Warning: Code in `easy_tbot.contrib.bot,aiogram` requires `aiogram>=2.12`.")
    print("FIX: You can install it with `pip install easy_tbot[aiogram]`.")
    raise

from ._backend import AiogramBackend