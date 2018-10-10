import abc as _abc
from abc import ABC as _AbstractClass


class Metric(_AbstractClass):
    def __init__(self):
        pass

    @_abc.abstractmethod
    def _eval(self, r):
        ...

    def __call__(self, r):
        return self._eval(r)
