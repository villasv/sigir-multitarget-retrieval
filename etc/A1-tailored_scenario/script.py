import numpy as np

from germs.functions import *
from germs.metrics.ndcg import NDCG


def Us(k):
    def u_at_k(r):
        rk = np.asfarray(r)[:k]
        return np.sum(np.sort(rk)[-3:]) - k
    return u_at_k

def Uo(r, h=100):
    return max([Us(k)(r) for k in range(min(len(r),h))])

def run():
    R_g = np.pad(np.array([0,0,0,2,2,3,1,0,0,0]), (0, 10**6), 'constant')
    R_b = np.pad(np.array([3,1,0,0,1,1,0,0,0,0]), (0, 10**6), 'constant')

    print("Evaluation")
    ndcg = NDCG(3, identity, p1log2)
    print("NDCG@3/l/log2(1+i)       \t Lg = {:.3f} \t Lb = {:.3f}".format(ndcg(R_g), ndcg(R_b)))
    ndcg = NDCG(5, identity, p1log2)
    print("NDCG@5/l/log2(1+i)       \t Lg = {:.3f} \t Lb = {:.3f}".format(ndcg(R_g), ndcg(R_b)))
    ndcg = NDCG(10, identity, p1log2)
    print("NDCG@10/l/log2(1+i)      \t Lg = {:.3f} \t Lb = {:.3f}".format(ndcg(R_g), ndcg(R_b)))

    print()

    ndcg = NDCG(3, exp2m1, p1log2)
    print("NDCG@3/2^l-1/log2(1+i)   \t Lg = {:.3f} \t Lb = {:.3f}".format(ndcg(R_g), ndcg(R_b)))
    ndcg = NDCG(5, exp2m1, p1log2)
    print("NDCG@5/2^l-1/log2(1+i)   \t Lg = {:.3f} \t Lb = {:.3f}".format(ndcg(R_g), ndcg(R_b)))
    ndcg = NDCG(10, exp2m1, p1log2)
    print("NDCG@10/2^l-1/log2(1+i)  \t Lg = {:.3f} \t Lb = {:.3f}".format(ndcg(R_g), ndcg(R_b)))

    print()

    u = Us(3)
    print("Us@3     \t Lg = {:.3f} \t Lb = {:.3f}".format(u(R_g), u(R_b)))
    u = Us(5)
    print("Us@5     \t Lg = {:.3f} \t Lb = {:.3f}".format(u(R_g), u(R_b)))
    u = Us(10)
    print("Us@10    \t Lg = {:.3f} \t Lb = {:.3f}".format(u(R_g), u(R_b)))

    u = Uo
    print("Uo       \t Lg = {:.3f} \t Lb = {:.3f}".format(u(R_g), u(R_b)))


if __name__ == "__main__":
    run()
