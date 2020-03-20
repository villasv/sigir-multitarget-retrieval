class DCG(Metric):
    def __init__(self, k=None, G=identity, D=p1log2):
        self._k = k
        self._G = G
        self._D = D

    def _eval(self, r):
        r = np.asfarray(r)
        k = self._k if self._k is not None else r.size
        rk = r[:k]
        return np.sum(self._G(rk) / self._D(np.arange(1, k + 1)))


class NDCG(Metric):
    def __init__(self, k=None, G=identity, D=p1log2):
        self._dcg = DCG(k, G, D)

    def _eval(self, r):
        max_dcg = self._dcg(sorted(r, reverse=True))
        return max_dcg and (self._dcg(r) / max_dcg)
