#!/usr/bin/env python3
import sys

color_index = (0,1,9,2,10,3,11,4,12,5,13,6,7,8,14,15)
#color_index = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

def rgb(r, g, b):
    print('#' + ''.join('%02x'%i for i in [r, g, b]))
    return

def main():
    if len(sys.argv) < 2:
        print('usage: ' + sys.argv[0] + ' filename\n')
        return -1

    f_in = open(sys.argv[1], 'r')
    if not f_in:
        print('failed\n')
        return -2

    scheme = f_in.readline()
    if not scheme:
        print('failed (2)\n')
        return -3

    f_in.close()

    scheme = eval(scheme)

    for c, color in enumerate(scheme):
        c2 = color_index[c]
        print(f"color{c2} ", end='')
        eval(color)

    f_in = open('kitty.defaults', 'r')
    if not f_in:
        print('missing kitty.defaults\n')
        return -4

    line = f_in.readline()
    while(line != ""):
        print(line, end='')
        line = f_in.readline()

    f_in.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())

