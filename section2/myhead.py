# -*- coding: utf-8 -*-

import sys


def my_head(target:str, N:int):
    with open(file=target, mode='r', encoding='utf-8') as f:
        for i in range(N):
            if (line := f.readline()):
                print(line, end='')

if __name__ == '__main__':
    my_head(sys.argv[1], int(sys.argv[2]))