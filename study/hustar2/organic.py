# 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    M, N, K = map(int, input().split())

    mat = [[0]*N for _ in range(M)]

    for _ in range(K):
        X, Y = map(int, input().split())
        mat[X][Y] = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    stack = []
    count = 0

    for X in range(M):
        for Y in range(N):
            if mat[X][Y] == 1:
                stack.append((X, Y))
                while len(stack) > 0:
                    x, y = stack.pop()
                    mat[x][y] = 0

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if (nx >= 0 and nx < M and ny >= 0 and ny < N):
                            if mat[nx][ny] == 1:
                                mat[nx][ny] = 0
                                stack.append((nx, ny))
                count += 1

    print(count)
