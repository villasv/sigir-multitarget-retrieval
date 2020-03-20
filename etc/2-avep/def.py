
class AveP(Metric):
    def __init__(self, ylim, k=None):
        self._ylim = ylim
        self._k = k

    def _eval(self, r):
        r = np.asfarray(r)
        k = self._k if self._k is not None else r.size
        rk = r[:k]
        n_pos = np.sum(rk >= self._ylim)
        if n_pos < 1:
            return 0

        patks = 0
        for i in range(k):
            if rk[i] >= self._ylim:
                patks += PatK(self._ylim, i+1)(rk)
        return patks / n_pos
