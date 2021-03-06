# -*- coding: utf-8 -*-
#
from .helpers import _s3, _s21
from ..helpers import untangle


class HammerStroud(object):
    '''
    Preston C. Hammer and Arthur H. Stroud,
    Numerical Evaluation of Multiple Integrals II,
    Math. Comp. 12 (1958), 272-280,
    <https://doi.org/10.1090/S0025-5718-1958-0102176-6>.
    '''
    def __init__(self, degree):
        self.degree = degree
        if degree == 2:
            data = [
                (1.0/3.0, _s21(1.0/6.0)),
                ]
        else:
            assert degree == 3
            data = [
                (-27.0/48.0, _s3()),
                (+25.0/48.0, _s21(0.2)),
                ]

        self.bary, self.weights = untangle(data)
        self.points = self.bary[:, 1:]
        return
