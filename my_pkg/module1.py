#!/usr/bin/python3

def bin_changer (num):
    d = int(num,2)
    o = oct(d)
    h = hex(d)
    

    print('oct: '+o)
    print('hex: '+h)
    print('dec: %d'%(d))
