#!/usr/bin/python3
if __name__ == "__main__"
    import sys
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 0:
        print("No arguments were passed")
    else:
        for i in range(num_args):
            print(i + 1, ":", args[i])
            print("")
