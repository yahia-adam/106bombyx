#!/usr/bin/env python3
import sys

def calc_x_plus_one(k, xi):
    xi = k * xi * (1000 - xi) / 1000
    return (xi)

def curve_generation():
    n = float(sys.argv[1])
    k = float(sys.argv[2])
    i = 0
    xi = n
    while (i != 100):
        i = i + 1
        print(i, "{:.2f}" .format(xi))
        xi = calc_x_plus_one(k, xi)