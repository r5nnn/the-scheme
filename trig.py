import math as maths


def sine():
    for i in range(-360, 361):
        print(maths.sin(maths.radians(float(i))))


def cosine():
    for i in range(-360, 361):
        print(maths.cos(maths.radians(float(i))))


def tangent():
    for i in range(-360, 361):
        print(maths.tan(maths.radians(float(i))))


cosine()