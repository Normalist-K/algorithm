import sys

sys.stdin = open("06-6.txt", "r")


class CircularQueuePython():
    def __init__(self):
        self.queue = []

    def enQueue(self, item):
        self.queue.append(item)

    def deQueue(self):
        if self.isEmpty():
            return None
        else:
            return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)

    def Qpeek(self):
        if self.isEmpty():
            return None
        else:
            return self.queue[0]


def BFS_short_way(maze, q):
    depth = -1  # 최단거리 초기화
    visited = []  # 방문 목록

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while True:
        if q.isEmpty():
            return 0  # queue가 비어있으면 갈 곳이 더이상 없다는 의미이므로 0 출력
        else:
            depth += 1
            num_candidates = q.length()
            for _ in range(num_candidates):
                i, j = q.deQueue()  # deQueue 하면 이동
                # if maze[i][j] == 3:  # 이동한 칸이 3이면 depth 출력
                #     return depth - 1
                visited.append((i, j))  # 방문 목록에 추가
                for idx in range(4):
                    ni = i + di[idx]
                    nj = j + dj[idx]
                    # 미로 밖을 벗어나는지 확인
                    if ni >= 0 and ni < len(maze) and nj >= 0 and nj < len(maze):
                        # 새 경로의 값이 0이나 3이고 방문한 적이 없다면
                        if (maze[ni][nj] == 3):
                            return depth
                        if (maze[ni][nj] == 0) and ((ni, nj) not in visited):
                            q.enQueue((ni, nj))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    maze = []

    q = CircularQueuePython()  # candidates

    for i in range(N):
        row = []
        for j, value in enumerate(input()):
            row.append(int(value))
            if value == "2":
                start = (i, j)
                q.enQueue(start)
        maze.append(row)

    result = BFS_short_way(maze, q)  # 끝지점에 도달하면 최단 거리 출력, 갈 곳이 더 이상 없으면 0 출력

    print(f"#{test_case} {result}")
