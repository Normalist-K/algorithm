import sys

sys.stdin = open("07-7.txt", "r")


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

    # pre_node 오른쪽에 새 노드 생성
    def add(self, pre_node, data):
        # 빈 노드가 들어오면 예외처리
        if pre_node == None:
            return None
        else:
            # 받아온 노드가 마지막 노드인 경우
            if pre_node == self.rear:
                self.rear = Node(data, pre_node, self.head)
                pre_node.post_link = self.rear
            # 받아온 노드가 중간에 위치한 노드인 경우
            else:
                new_node = Node(data, pre_node, pre_node.post_link)
                new_node.pre_link.post_link = new_node
                new_node.post_link.pre_link = new_node
            # 길이 1 추가
            self.length += 1

    def addToLast(self, data):
        # 빈 리스트인 경우
        if self.head == None:
            new_node = Node(data, None, None)
            new_node.post_link = new_node  # post_link로 자기 자신을 가리키도록
            self.head = new_node
            self.rear = new_node
            self.length += 1
        # 빈 리스트가 아닌 경우
        else:
            last_node = self.rear
            # 마지막 노드의 post는 첫 노드를 가리키도록
            new_node = Node(data, last_node, self.head)
            self.rear = new_node
            last_node.post_link = new_node
            self.length += 1

    def get(self, idx):  # idx를 받아 해당 idx의 node 출력
        if idx >= self.length:
            return None
        else:
            target_node = self.head
            if idx > 0:
                for _ in range(idx):
                    target_node = target_node.post_link
            return target_node

    # 이동할 칸 수 -1 이동 후 오른쪽에 새 노드를 추가하고 해당 노드를 출력
    def AddAfterMove(self, current_node, M):
        for _ in range(M - 1):
            current_node = current_node.post_link
        new_data = current_node.data + current_node.post_link.data
        self.add(current_node, new_data)
        return current_node.post_link


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    # N: 자연수 개수, M: 추가할 칸이 몇 번째 칸인지, K: 반복 횟수
    N, M, K = map(int, input().split())

    # N개의 자연수를 받아서 링크드 리스트 생성
    L = LinkedList()
    for num in map(int, input().split()):
        L.addToLast(num)

    current_node = L.get(0)
    for _ in range(K):
        current_node = L.AddAfterMove(current_node, M)

    if L.length > 10:
        L.length = 10

    print(f"#{test_case}", end=' ')
    last_node = L.rear
    for _ in range(L.length):
        print(last_node.data, end=" ")
        last_node = last_node.pre_link
    print()
