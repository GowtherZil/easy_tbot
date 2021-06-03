#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('BOT_SETTING_MODULE', 'settings')
    from easy_tbot.core.cli.shortcuts import handle
    handle(sys.argv[1:])

if __name__ == '__main__':
    main()