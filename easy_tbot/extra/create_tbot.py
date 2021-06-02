from .tpl import create_project
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('name', type=str)
    ap.add_argument('token', type=str, default='')
    ne = ap.parse_args()
    create_project(ne.name, ne.token)