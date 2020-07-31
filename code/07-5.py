import sys

sys.stdin = open("07-5.txt", "r")


class Node():
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link


class SimpleLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    def addToFirst(self, data):
        self.head = Node(data, self.head)
        self.length += 1

    def add(self, pre_node, data):
        if pre_node == None:
            return None
        else:
            pre_node.link = Node(data, pre_node.link)
            self.length += 1

    def addToLast(self, data):
        if self.head == None:
            self.head = Node(data, self.head)
            self.length += 1
        else:
            # last_node: 첫 노드에서 시작해서 while 돌면서 계속 마지막 원소로 이동
            last_node = self.head
            while last_node.link != None:
                last_node = last_node.link
            last_node.link = Node(data, None)
            self.length += 1

    def deleteToFirst(self):
        if self.head == None:
            return None
        else:
            self.head = self.head.link
            self.length -= 1

    def delete(self, pre_node):
        if pre_node == None:
            return None
        else:
            pre_node.link = pre_node.link.link
            self.length -= 1

    def get(self, idx):
        if idx >= self.length:
            return None
        else:
            target_node = self.head
            if idx > 0:
                for _ in range(idx):
                    target_node = target_node.link
            return target_node


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    first_len, times, out_idx = map(int, input().split())

    nums = SimpleLinkedList()

    for num in list(map(int, input().split()))[::-1]:
        nums.addToFirst(num)

    for _ in range(times):
        idx, new_num = map(int, input().split())
        nums.add(nums.get(idx - 1), new_num)

    result = nums.get(out_idx).data

    print(f"#{test_case} {result}")
