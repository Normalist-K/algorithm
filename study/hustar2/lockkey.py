def check(key, lock, i, j, M, N):
    for x in range(M):
        for y in range(M):
            ni = i + x
            nj = j + y
            if (ni not in range(N)) or (nj not in range(N)):
                continue
            chk = lock[ni][nj] + key[x][y]
            if chk in (0, 2):
                return False
    return True


def solution(key, lock):

    M = len(key)
    N = len(lock)

    zeros_i = []
    zeros_j = []

    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                zeros_i.append(i)
                zeros_j.append(j)

    if zeros_i == []:
        return True

    left, right = min(zeros_j), max(zeros_j)
    up, down = min(zeros_i), max(zeros_i)

    if (right - left - 1 > M) or (down - up - 1) > M:
        return False

    for _ in range(4):
        key = list(zip(*key[::-1]))
        for i in range(down-M+1, up+1):
            for j in range(right-M+1, left+1):
                if check(key, lock, i, j, M, N):
                    return True
    return False


print(min([]))
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
