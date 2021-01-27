#!/usr/bin/env python3
import sys

# ColorPalette=#2e3436;#ff6363;#80fc41;#fff556;#6b9cff;#50ffd0;#c891ff;#aaaaaa;#636363;#ff9191;#bdff9c;#fffaaf;#a0bfff;#b4ffeb;#e4c8ff;#e1e1e1;

def main():
    f_in = open("theme.sh", 'r')
    if not f_in:
        print('open theme.sh failed\n')
        return -1
    
    fn_s = f_in.readline()
    while fn_s:
        # seek past 'themes=...' line
        if fn_s[0:7] == "themes=":
            break
        fn_s = f_in.readline()
        
    if not fn_s:
        print('find themes= failed\n')
        return -2

    fn_s = f_in.readline().strip()
    while fn_s:
        # end of theme list
        if fn_s[0] == ')':
            break

        # this format is easier
        f_out = open(fn_s + ".xfce.pal", 'w')
        f_out.write('ColorPalette=')
        for c_n in range(16):
            col = f_in.readline().strip().split(':')[1][1:]
            f_out.write(col + ';')
        f_out.write('\n')
        f_out.close()

        # skip to next theme 
        for c_n in range(4):
            f_in.readline()
        fn_s = f_in.readline().strip()

    f_in.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())

