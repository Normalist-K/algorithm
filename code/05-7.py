import sys

sys.stdin = open("sample_input.txt", "r")


def construct_candidates(a, k, n, c):
    in_perm = [False] * (n + 1)

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(0, n):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates


def backtrack(mat, a, k, n, result):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == n:
        total = 0
        for i in range(1, k + 1):
            total += mat[i - 1][a[i]]
        result.append(total)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(mat, a, k, n, result)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    MAXCANDIDATES = 120
    a = [0] * (N + 1)
    result = []
    backtrack(mat, a, 0, N, result)

    print(f"#{test_case} {min(result)}")
