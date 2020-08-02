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
            self.rear = self.head
        else:
            last_node = self.rear
            self.rear = Node(data, last_node, None)
            last_node.post_link = self.rear
            self.length += 1

    def addToLeft(self, post_node, data):
        if post_node == None:
            return None
        else:
            if post_node.pre_link == None:
                new_Node = Node(data, pre_link=None, post_link=post_node)
                post_node.pre_link = new_Node
                self.head = new_Node
            else:
                new_Node = Node(data, pre_link = post_node.pre_link, post_link = post_node)
                post_node.pre_link.post_link = new_Node
                post_node.pre_link = new_Node

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

    def getByNum(self, num):  # 숫자를 받아 해당 숫자보다 큰 숫자의 node를 출력
        if self.length == 0:
            return print('error')
        compare_node = self.head
        while not (compare_node.data > num):
            if compare_node == self.rear:
                return None
            compare_node = compare_node.post_link
        return compare_node


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    len_nums, count_nums = map(int, input().split())

    target_nums = LinkedList()

    # 첫 수열을 linked List에 저장
    for num in list(map(int, input().split())):
        target_nums.addToLast(num)

    # # linked list 확인용
    # node = target_nums.head
    # print(node.data, end=',')
    # for _ in range(target_nums.length - 1):
    #     node = node.post_link
    #     print(node.data, end=',')
    # print()
    
    for _ in range(count_nums - 1):
        nums_to_add = list(map(int, input().split()))
        post_node = target_nums.getByNum(nums_to_add[0])
        if post_node != None:
            for num in nums_to_add:
                target_nums.addToLeft(post_node, num)
        else:
            for num in nums_to_add:
                target_nums.addToLast(num)
        
    # 결과 출력: 뒤에서부터 10자리까지
    print(f"#{test_case}", end=' ')
    last_node = target_nums.rear
    for _ in range(10):
        print(last_node.data, end=" ")
        last_node = last_node.pre_link
    print()
