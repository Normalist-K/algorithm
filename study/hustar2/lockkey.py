import numpy as np


def check()


def solution(key, lock):
    key = np.array(key)
    lock = np.array(lock)

    M = len(key)
    N = len(lock)

    pad_lock = np.pad(lock, ((M-1, M-1), (M-1, M-1)),
                      'constant', constant_values=(-1))

    for i in range(N-M+1):
        for j in range(N-M+1):


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
