import sys

sys.stdin = open("08-6.txt", "r")


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def visit(data, count):
    count.append(data)


def preorder_traverse(node, count):
    if node == None:
        return
    visit(node.data, count)
    preorder_traverse(node.left, count)
    preorder_traverse(node.right, count)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    E, N = map(int, input().split())

    e = list(map(int, input().split()))
    tree = [Node(i+1) for i in range(E+2)]

    for i in range(0, len(e), 2):
        if tree[e[i]].left == None:
            tree[e[i]].left = tree[e[i + 1]]
        else:
            tree[e[i]].right = tree[e[i + 1]]

    count = []
    preorder_traverse(tree[N], count)

    print(f"#{test_case} {len(count)}")
