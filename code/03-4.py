import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    NN = []
    for i in range(N):
        NN.append(input())

    isFind_c = 0
    isFind_r = 0

    # 가로 순회
    for i in range(N):
        for j in range(N - M + 1):
            for n in range(M//2):
                if NN[i][j + n] == NN[i][j + M - 1 - n]:
                    isFind_c += 1
                    if isFind_c == M//2:
                        print(f"#{test_case} {NN[i][j:j + M]}")
                else:
                    isFind_c = 0
                    break
    # 세로 순회
    for i in range(N - M + 1):
        for j in range(N):
            for n in range(M//2):
                if NN[i + n][j] == NN[i + M - 1 - n][j]:
                    isFind_r += 1
                    if isFind_r == M//2:
                        s = ''
                        for row in NN[i:i + M]:
                            s += row[j]
                        print(f"#{test_case} {s}")
                else:
                    isFind_r = 0
                    break
