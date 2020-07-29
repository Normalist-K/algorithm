import sys

sys.stdin = open("sample_input.txt", "r")


class Stack:
    stackList = []

    def push(self, item):
        self.stackList.append(item)

    def pop(self):
        if len(self.stackList) <= 0:
            return None
        return self.stackList.pop()

    def clear(self):
        self.stackList.clear()

    def len(self):
        return len(self.stackList)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    maze = [list(map(int, input())) for i in range(N)]

    stack = Stack()
    stack.clear()

    # 시작점 찾아서 stack에 넣기
    for i in range(len(maze)):
        if 2 in maze[i]:
            j = maze[i].index(2)
            stack.push((i, j))

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    isFind = 0
    # stack에서 pop하면 이동, 이동 후 4방향 비교해서 길 있으면 push
    # 더 이상 갈 길이 없거나 end point 찾으면 중단
    while stack.len() > 0:
        i, j = stack.pop()
        maze[i][j] = 1  # end point가 아니라면 이동한 지금은 벽으로 바꾸기
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if (ni >= 0 and ni < N and nj >= 0 and nj < N):  # 미로를 벗어나지 않는지 체크
                if maze[ni][nj] == 3:  # 이동할 지점이 end point 인지 확인
                    print(f"#{test_case} 1")
                    isFind = 1
                    break
                if maze[ni][nj] == 0:
                    stack.push((ni, nj))

    if isFind == 0:
        print(f"#{test_case} 0")
