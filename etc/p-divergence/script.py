import random

import numpy as np
import pandas as pd
import seaborn as sns


class Metric:
    def __init__(self):
        pass

    def _eval(self, r):
        ...

    def __call__(self, r):
        return self._eval(r)


class PatK(Metric):
    def __init__(self, k, ylim):
        self._k = k
        self._ylim = ylim

    def _eval(self, r):
        r = np.asfarray(r)
        if r.size < self._k:
            _log.warning("Metric expected more points than provided")

        rk = r[:self._k]
        return np.sum(rk >= self._ylim) / self._k


random.seed(42)
patk_05 = PatK(k=5, ylim=5)
patk_10 = PatK(k=10, ylim=5)
patk_50 = PatK(k=50, ylim=5)


def gen_ranking(n):
    return np.clip(np.rint(np.random.normal(0, 3, n)), 0, 10)


def main():
    sampling = 100
    linspace = [int(i) for i in np.rint(np.linspace(10**2, 10**4, num=100))]
    rankings = [gen_ranking(n) for n in linspace for _ in range(sampling)]

    df = pd.DataFrame(
        [[r.size, '05', patk_05(r)] for r in rankings] +
        [[r.size, '10', patk_10(r)] for r in rankings] +
        [[r.size, '50', patk_50(r)] for r in rankings],
        columns=['N', 'k', 'P at k']
    )
    sns.lineplot(x='N', y='P at k', hue='k', ci='sd', data=df).get_figure().savefig('patk.png')
    return df


if __name__ == "__main__":
    main()
