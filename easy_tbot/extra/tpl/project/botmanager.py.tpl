#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('BOT_SETTING_MODULE', 'settings')
    from easy_tbot.core.cli import loader
    loader().handle_input(sys.argv[1:])

if __name__ == '__main__':
    main()