#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

try:
    input = raw_input
except NameError:
    pass

def get_numeric_value(prompt):
    """
    Requests a numeric value from the standard input.
    Returns None if no value was inserted.
    """
    while True:
        value = input(prompt)
        if not value:
            return None
        try:
            value = int(value)
        except ValueError:
            print("Debe ingresar un valor numerico. "
                  "Vuelva a intentarlo.")
        else:
            break
    return value

def get_triangle(a=None, b=None, h=None):
    """
    Returns a triangle string, with the specified values.
    """
    return r"""
    |\
    | \
    |  \ h
  a |   \
    |    \
    |_ _ _\
      b
    
    a = %s
    b = %s
    h = %s""" % ("?" if a is None else a,
                 "?" if b is None else b,
                 "?" if h is None else h)

def main():
    print(get_triangle())
    print("\nDeje en blanco el valor que desconoce.\n")
    
    a = get_numeric_value("a: ")
    b = get_numeric_value("b: ")
    
    if a is None or b is None:
        h = get_numeric_value("h: ")
    else:
        h = None
    
    if (bool(a) + bool(b) + bool(h)) < 2:
        print("Debe especificar, al menos, dos valores.")
        return 0
    
    if h is None:
        h = sqrt(a**2 + b**2)
    elif a is None:
        a = sqrt(h**2 - b**2)
    elif b is None:
        b = sqrt(h**2 - a**2)
    
    print("")
    print(get_triangle(a, b, h))
    
    return 0

if __name__ == '__main__':
    main()
