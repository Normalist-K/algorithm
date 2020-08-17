import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


def inorder_traverse(N, indexNode, value, listNode):
    if indexNode > N:
        return value

    listNode[indexNode] = inorder_traverse(
        N, indexNode * 2, value, listNode) + 1

    return inorder_traverse(N, indexNode * 2 + 1, listNode[indexNode], listNode)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    listNode = [None for _ in range(N + 1)]

    inorder_traverse(N, 1, 0, listNode)

    # print(f"#{test_case} {listNode[1]} {listNode[N//2]}")
    print(f"#{test_case} {listNode}")
