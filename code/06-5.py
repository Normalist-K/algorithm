import sys

sys.stdin = open("sample_input.txt", "r")


class CircularQueuePython():
    def __init__(self):
        self.queue = []

    def set_queue(self, data):
        self.queue = data

    def enQueue(self, item):
        self.queue.append(item)

    def deQueue(self):
        if self.isEmpty():
            return None
        else:
            return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def Qpeek(self):
        if self.isEmpty():
            return None
        else:
            return self.queue[0]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    q = CircularQueuePython()

    nums = list(map(int, input().split()))
    q.set_queue(nums)

    for _ in range(M):
        q.enQueue(q.deQueue())

    print(f"#{test_case} {q.deQueue()}")
