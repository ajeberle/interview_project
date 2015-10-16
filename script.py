#!/usr/bin/python
import sys
def main():
    args = sys.argv
    if len(args) != 2:
        return 1
    if args[1] != "continue":
        print "Incorrect input"
        return 1
    print "Correct"
    return 0

if __name__ == "__main__":
    sys.exit(main())
