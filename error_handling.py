#!/usr/bin/env python3
from calendar import TUESDAY
import re
import sys
import string
import math

def check_int(str : string):
    for m in range(len(str)):
        if str[m] > '9' or str[m] < '0':
            return (0)
    return (1)

def check_float(str: string):
    for m in range(len(str)):
        if str[m] != '.' and (str[m] > '9' or str[m] < '0'):
            return (0)
    return (1)

def error_handling():
    if (len(sys.argv) != 3 and len(sys.argv) != 4):
        return (84)
    for i in  range(len(sys.argv)):
        if (check_float(sys.argv[i])) == 0:
            return (84)
    if len(sys.argv) == 3:
        if check_float(sys.argv[1]) == 0:
            sys.exit(84)
        if (float(sys.argv[1]) <= 0):
            sys.exit(84)
        if float(sys.argv[2]) < 1 or float(sys.argv[2]) > 4:
            sys.exit(84)
    if len(sys.argv) == 4:
        if check_float(sys.argv[1]) == 0:
            sys.exit(84)
        if (float(sys.argv[1]) <= 0):
            sys.exit(84)
