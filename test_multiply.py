# coding:utf-8

import numpy as np
import test

def _main():
    x=np.ones(10,dtype=np.int16)*100
    print(x)
    test.multiply(x)
    print(x)
    return

if __name__ == "__main__" : _main()
