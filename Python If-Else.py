#!/bin/python3

import math
import os
import random
import re
import sys

def isEven(numb):
    result = bool( ( numb % 2 ) == 0 )
    return result

if __name__ == '__main__':
    n = int(input().strip())
    if isEven(n) and ( n > 20 ):
        print("Not Weird")
    elif isEven(n) and ( n > 6 ):
        print("Weird")
    elif isEven(n) and ( n > 1):
        print("Not Weird")
    else:
        print("Weird")
    

