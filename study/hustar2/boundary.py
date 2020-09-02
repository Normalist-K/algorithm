# 영역 구하기
# https://www.acmicpc.net/problem/2583
import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local', 'DESKTOP-7IAC63A'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

M, N, K = map(int, input().split())

mat = [[1]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            mat[x][y] = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

stack = []
count = 0
size = []
size_buffer = 0

for X in range(M):
    for Y in range(N):
        if mat[X][Y] == 1:
            stack.append((X, Y))
            while len(stack) > 0:
                size_buffer += 1
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
            size.append(size_buffer)
            size_buffer = 0

print(count)
size.sort()
print(*size)