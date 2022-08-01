#!/usr/bin/env python3
import sys
import generation_curve

def calc_x_plus_one(k : int, xi : int) -> int:
    xi = k * xi * (1000 - xi) / 1000
    return (xi)

def sum_n():
    xi = float(sys.argv[2])
    xf = float(sys.argv[3])
    x = float(sys.argv[1])
    k = 100
    i = 1
    while k <= 400:
        i = 1
        while i <= xf:
            while(i < xi):
                x = generation_curve.calc_x_plus_one((k / 100), x)
                i = i + 1
            x = generation_curve.calc_x_plus_one((k / 100), x)
            print("{:.2f} ""{:.2f}" .format((k / 100), x))
            i = i + 1
        k = k + 1
