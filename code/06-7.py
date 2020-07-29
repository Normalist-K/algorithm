import sys

sys.stdin = open("sample_input.txt", "r")


class CircularQueue():

    listData = []
    front = 0
    rear = 0

    def __init__(self, size):
        self.listData = [0 for _ in range(size + 1)]
        self.front = 0
        self.rear = 0

    def enQueue(self, item):
        if self.isFull():
            print("Queue_Full")
        else:
            self.rear = (self.rear + 1) % len(self.listData)
            self.listData[self.rear] = item

    def deQueue(self):
        if self.isEmpty():
            print("Queue_Empty")
        else:
            self.front = (self.front + 1) % len(self.listData)
            return self.listData[self.front]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % len(self.listData) == self.front

    def Qpeek(self):
        if self.isEmpty():
            print("Queue_Empty")
        else:
            return self.listData[self.front + 1]


def last_pizza(N, q, pizzas):
    # 화덕 수 만큼 피자 넣기
    for _ in range(N):
        q.enQueue(pizzas.pop())

    # 모든 피자를 화덕에 넣고, 모든 피자를 다 꺼낼 때 까지 체크 반복
    while not q.isEmpty():
        idx, cheeze = q.deQueue()
        cheeze //= 2
        if cheeze == 0:
            if len(pizzas) != 0:
                q.enQueue(pizzas.pop())
            else:
                last_pizza = idx
        else:
            q.enQueue([idx, cheeze])

    return last_pizza


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    pizzas = [[idx + 1, cheeze]
              for idx, cheeze in enumerate(list(map(int, input().split())))]

    q = CircularQueue(N)

    result = last_pizza(N, q, pizzas[::-1])

    print(f"#{test_case} {result}")
