import sys

sys.stdin = open("07-8 copy.txt", "r")


class Node():
    def __init__(self, data, pre_link=None, post_link=None):
        self.data = data
        self.pre_link = pre_link
        self.post_link = post_link


class LinkedList():
    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    # 리스트 맨 앞에 추가
    def addToFirst(self, data):
        new_node = Node(data, None, self.head)
        if self.length == 0:
            self.head = new_node
            self.rear = new_node
        else:
            self.head.pre_link = new_node
            self.head = new_node
        self.length += 1

    # 리스트 맨 마지막에 추가
    def addToLast(self, data):
        new_node = Node(data, self.rear, None)
        if self.length == 0:
            self.head = new_node
            self.rear = new_node
        else:
            self.rear.post_link = new_node
            self.rear = new_node
        self.length += 1

    # node를 입력받아 해당 노드 왼쪽에 추가
    def add(self, post_node, data):
        if post_node == None:
            return None
        else:
            if post_node == self.head:
                self.addToFirst(data)
            else:
                new_node = Node(data, post_node.pre_link, post_node)
                post_node.pre_link = new_node
                new_node.pre_link.post_link = new_node
                self.length += 1

    # idx를 받아서 해당 노드 왼쪽에 새 노드 생성
    def addByIdx(self, idx, data):
        if idx == self.length:
            self.addToLast(data)
        else:
            target_node = self.get(idx)
            # 에러처리 (인덱스가 범위를 초과하거나, 빈 리스트인 경우)
            if target_node == -1 and self.length == 0:
                return None
            else:
                self.add(target_node, data)

    # 첫번째 노드를 삭제
    def deleteToFirst(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.rear = None
            self.length = 0
        else:
            self.head = self.head.post_link
            self.head.post_link.pre_link = None
            self.length -= 1

    # 입력받은 노드의 왼쪽 노드를 삭제
    def deleteLeft(self, post_node):
        if post_node == None and post_node.pre_link == None:
            return None
        else:
            target_node = post_node.pre_link
            post_node.pre_link = target_node.pre_link
            target_node.pre_link.post_link = post_node
            self.length -= 1

    # 입력받은 노드를 삭제
    def delete(self, target_node):
        if target_node == None and self.length == 0:
            return None
        if self.length == 1 and target_node == self.head:
            self.head = None
            self.rear = None
            self.length = 0
        else:
            if target_node == self.head:
                self.head = target_node.post_link
                target_node.post_link.pre_link = None
            elif target_node == self.rear:
                self.rear = target_node.pre_link
                target_node.pre_link.post_link = None
            else:
                target_node.post_link.pre_link = target_node.pre_link
                target_node.pre_link.post_link = target_node.post_link
            self.length -= 1

    # 마지막 노드를 삭제
    def deleteToLast(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.rear = None
            self.length = 0
        else:
            self.rear = self.rear.pre_link
            self.rear.pre_link.post_link = None
            self.length -= 1

    # idx를 받아서 해당 노드 삭제
    def deleteByIdx(self, idx):
        target_node = self.get(idx)
        # 에러처리 (인덱스가 범위를 초과하거나, 빈 리스트인 경우)
        if target_node == -1 and self.length == 0:
            return None
        else:
            self.delete(target_node)

    # idx를 받아서 해당 노드 변경
    def change(self, idx, data):
        target_node = self.get(idx)
        # 에러처리 (인덱스가 범위를 초과하거나, 빈 리스트인 경우)
        if target_node == -1 and self.length == 0:
            return None
        else:
            target_node.data = data

    # idx를 받아서 해당 노드 리턴, 없으면 -1
    def get(self, idx):
        if idx >= self.length:
            return -1
        else:
            if idx == 0:
                return self.head
            elif idx == self.length - 1:
                return self.rear
            else:
                target_node = self.head
                for _ in range(idx):
                    target_node = target_node.post_link
                return target_node

    # idx를 받아서 해당 노드의 data를 리턴, 없으면 -1
    def getData(self, idx):
        target_node = self.get(idx)
        if target_node == -1:
            return -1
        else:
            return target_node.data


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M, L = map(int, input().split())

    nums = LinkedList()

    # 수열을 받아서 Linked List에 저장
    for num in map(int, input().split()):
        nums.addToLast(num)

    for _ in range(M):
        commands = list(input().split())
        if commands[0] == 'I':
            nums.addByIdx(int(commands[1]), int(commands[2]))
        elif commands[0] == 'D':
            nums.deleteByIdx(int(commands[1]))
        elif commands[0] == 'C':
            nums.change(int(commands[1]), int(commands[2]))

    result = nums.getData(L)
    print(f"#{test_case} {result}")

    # for i in range(nums.length):
    #     print(f"{nums.getData(i)}", end=' ')
    # print()
