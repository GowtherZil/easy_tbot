"""
Module in charge of facilitating the use of databases
"""

# Like the other main modules of the kernel, this one is
# designed to wrap other libraries that facilitate work
# with different types of databases.

# We import main class (DataBase) as loader to outer scope
# this class handle all heavy lifting for the database
from ._loader import DataBase as loader
