#!/usr/bin/env python3
import sys

def rgb(r, g, b):
    print('#' + format(r, 'x') + format(g, 'x') + format(b, 'x') + ';', end='');
    return

def main():
    if len(sys.argv) < 2:
        print('usage: ' + sys.argv[0] + ' filename\n')
        return -1

    f_in = open(sys.argv[1], 'r')
    if not f_in:
        print('failed\n')
        return -2

    cs = f_in.readline()
    if not cs:
        print('failed (2)\n')
        return -3

    f_in.close()

    cs = eval(cs)

    print('ColorPalette=', end='')

    for c in cs:
        eval(c)

    print();

    return 0

if __name__ == '__main__':
    sys.exit(main())

