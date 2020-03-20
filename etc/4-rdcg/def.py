
class RDCG(Metric):
    def __init__(self, k=None, G=identity, D=p1log2):
        self._dcg = DCG(k, G, D)

    def _eval(self, r):
        max_dcg = self._dcg(sorted(r, reverse=True))
        min_dcg = self._dcg(sorted(r))
        a = (self._dcg(r) - min_dcg)
        b = (max_dcg - min_dcg)
        g['DONES'] += 1
        print(f"{g['DONES']}/{g['TOTAL']}")
        return a / b if b > 0 else 0
