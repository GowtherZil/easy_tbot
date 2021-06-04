"""
This module is designed to contain the main entry point associated with 
easy_tbot allowing us to create the folder structure associated with an 
easy_tbot project.
"""

# We import the function to create a project 
from .tpl import create_project
# and argparse for handle cli input
import argparse

# ##The entry point
# This *main* method work as a entry point to create a structure of folders associated with a project
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("name", type=str)
    ap.add_argument("token", type=str, default="")
    ne = ap.parse_args()
    create_project(ne.name, ne.token)