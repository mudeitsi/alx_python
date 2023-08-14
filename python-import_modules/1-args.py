#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc) if argc != 0 else "0 arguments.")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

