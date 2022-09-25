# -*- coding: utf-8 -*-

import sys


def my_tail(target:str, N:int):
    with open(file=target, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
    

if __name__ == '__main__':
    my_tail(sys.argv[1], int(sys.argv[2]))