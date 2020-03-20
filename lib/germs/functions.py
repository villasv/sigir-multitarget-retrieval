import numpy as _np


def identity(v):
    return _np.asfarray(v)


def exp2m1(v):
    return _np.exp2(v) - 1


def p1log2(v):
    return _np.log2(v + 1)
