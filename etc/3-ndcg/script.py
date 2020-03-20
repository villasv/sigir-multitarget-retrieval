import random

import numpy as np
import pandas as pd
import seaborn as sns


def identity(v):
    return np.asfarray(v)


def exp2m1(v):
    return np.exp2(v) - 1


def p1log2(v):
    return np.log2(v + 1)


class Metric:
    def __init__(self):
        pass

    def _eval(self, r):
        ...

    def __call__(self, r):
        return self._eval(r)


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


random.seed(42)
ndcg_nn = NDCG()
ndcg_05 = NDCG(k=5)
ndcg_50 = NDCG(k=50)


def gen_ranking(n):
    return np.clip(np.rint(np.random.normal(0, 3, n)), 0, 10)


def main():
    sampling = 100
    linspace = np.linspace(10 ** 2, 10 ** 4, num=100)
    ranksize = [int(i) for i in np.rint(linspace)]
    rankings = [gen_ranking(n) for n in ranksize for _ in range(sampling)]

    df = pd.DataFrame(
        [[r.size, "N", ndcg_nn(r)] for r in rankings]
        + [[r.size, "05", ndcg_05(r)] for r in rankings]
        + [[r.size, "50", ndcg_50(r)] for r in rankings],
        columns=["$N$", "$k$", "$NDCG@k$"],
    )
    sns.lineplot(
        x="$N$", y="$NDCG@k$", hue="$k$", ci="sd", data=df
    ).get_figure().savefig("ndcg.png")


if __name__ == "__main__":
    main()
