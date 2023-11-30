#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("{}".format(0))
    else:
        total = 0

        for i in range(count):
            total += int(sys.argv[i + 1])
        
        print("{}".format(total))
