import random

import numpy as np
import pandas as pd
import seaborn as sns

# ... metric defitions ...

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
        [[r.size, "=N", ndcg_nn(r)] for r in rankings]
        + [[r.size, "05", ndcg_05(r)] for r in rankings]
        + [[r.size, "50", ndcg_50(r)] for r in rankings],
        columns=["N", "k", "NDCG@k"],
    )
    sns.lineplot(
        x="N", y="NDCG@k", hue="k", ci="sd", data=df,
    ).get_figure().savefig("experiment.png")


if __name__ == "__main__":
    main()
