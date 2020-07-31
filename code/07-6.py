import sys

sys.stdin = open("07-6.txt", "r")


class Node():
    def __init__(self, data=None, pre_link=None, post_link=None):
        self.data = data
        self.pre_link = pre_link
        self.post_link = post_link


class LinkedList():
    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    def addToFirst(self, data):
        self.head = Node(data, None, self.head)
        if self.rear == None:
            self.rear = self.head
        self.length += 1

    def add(self, pre_node, data):
        if pre_node == None:
            return None
        else:
            if pre_node.post_link == None:
                self.rear = Node(data, pre_node, None)
                pre_node.post_link = self.rear
            else:
                pre_node.post_link = Node(data, pre_node, pre_node.post_link)
            self.length += 1

    def addToLast(self, data):
        if self.head == None:
            self.head = Node(data, None, self.head)
            self.length += 1
        else:
            last_node = self.rear
            self.rear = Node(data, last_node, None)
            last_node.post_link = self.rear
            self.length += 1

    def deleteToFirst(self):
        if self.head == None:
            return None
        else:
            first_node = self.head
            self.head = first_node.post_link
            first_node.post_link.pre_link = None
            self.length -= 1

    def delete(self, pre_node):
        if pre_node == None or pre_node.post_link == None:
            return None
        else:
            delete_node = pre_node.post_link
            if delete_node.post_link == None:
                self.rear = pre_node
                pre_node.post_link = None
            else:
                pre_node.post_link = delete_node.post_link
                delete_node.post_link.pre_link = pre_node
                self.length -= 1

    def get(self, idx):  # idx를 받아 해당 idx의 node 출력
        if idx >= self.length:
            return None
        else:
            target_node = self.head
            if idx > 0:
                for _ in range(idx):
                    target_node = target_node.post_link
            return target_node

    def getByNum(self, num):  # 숫자를 받아 해당 숫자보다 큰 숫자의 앞 숫자 node를 출력
        compare_node = self.head
        while True:
            if compare_node.post_link == None:
                return True
            if num >= compare_node.data:
                compare_node = compare_node.post_link
            else:
                if compare_node == self.head:
                    return False
                return compare_node.pre_link


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    len_nums, count_nums = map(int, input().split())

    target_nums = LinkedList()

    # 첫 수열을 linked List로 저장
    for num in list(map(int, input().split()))[::-1]:
        target_nums.addToFirst(num)

    for _ in range(count_nums - 1):
        nums_to_add = list(map(int, input().split()))
        pre_node = target_nums.getByNum(nums_to_add[0])
        if pre_node == True:
            for num in nums_to_add:
                target_nums.addToLast(num)
        elif pre_node == False:
            for num in nums_to_add[::-1]:
                target_nums.addToFirst(num)
        else:
            for num in nums_to_add:
                target_nums.add(pre_node, num)

    print(f"#{test_case}", end=' ')
    last_node = target_nums.rear
    for _ in range(10):
        print(last_node.data, end=" ")
        last_node = last_node.pre_link
    print()
