import logging as _log
import numpy as _np
import germs.functions as _f

from germs.metrics.base import Metric as _BaseMetric


class DCG(_BaseMetric):
    """
    """
    def __init__(self, k, G=_f.identity, D=_f.p1log2):
        self._k = k
        self._G = G
        self._D = D
    
    def _eval(self, r):
        r = _np.asfarray(r)
        if r.size < self._k:
            _log.warning("Metric expected more points than provided")

        rk = r[:self._k]
        return _np.sum(self._G(rk) / self._D(_np.arange(1, self._k + 1)))


class NDCG(_BaseMetric):
    """
    """
    def __init__(self, k, G=_f.identity, D=_f.p1log2):
        self._dcg = DCG(k, G, D)
    
    def _eval(self, r):
        max_dcg = self._dcg(sorted(r, reverse=True))
        return max_dcg and (self._dcg(r) / max_dcg)
