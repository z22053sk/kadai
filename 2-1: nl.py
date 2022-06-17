#課題1-2: nl.py
import sys

argc = len(sys.argv)
if argc == 1:
    f = sys.stdin
elif argc == 2:
    try:
        f = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("wc: No such file or directory,"+ sys.argv[1])
else:
    sys.exit("usage: wc [file]")

l = f.readlines()
f.close()

count = 0
for line in l:
    count = count + 1
    print(count, line)
