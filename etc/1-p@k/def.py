class PatK(Metric):
    def __init__(self, ylim, k=None):
        self._ylim = ylim
        self._k = k

    def _eval(self, r):
        r = np.asfarray(r)
        k = self._k if self._k is not None else r.size
        rk = r[:k]
        return np.sum(rk >= self._ylim) / k
