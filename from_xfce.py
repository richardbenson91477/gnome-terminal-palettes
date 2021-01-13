#!/usr/bin/env python3

import sys

header = 'ColorPalette='

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

    if cs[0:len(header)] != header:
        print('failed (3)\n')
        return -4

    print('[', end='')

    css = cs.split(header)[1].split('#')[1:]
    for i, s in enumerate(css):
        print('\'rgb(', end='')
        for n in (0, 2, 4):
            print(int(s[n] + s[n + 1], 16), end='')
            if n != 4:
                print (',', end='')
        if (i != len(css) - 1):
            print(')\', ', end='')
        else:
            print(')\']')

    return 0

if __name__ == '__main__':
    sys.exit(main())

