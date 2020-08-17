import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


def min_heap(list_node, num):
    list_node.append(num)

    last_index = len(list_node) - 1

    while last_index > 1:
        parent = list_node[last_index // 2]
        child = list_node[last_index]
        if parent > child:
            list_node[last_index // 2], list_node[last_index] = child, parent
        last_index //= 2


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    list_node = [None, ]
    for num in map(int, input().split()):
        min_heap(list_node, num)

    sum_parent = 0
    idx = N
    while idx > 1:
        sum_parent += list_node[idx // 2]
        idx //= 2

    print(f"#{test_case} {sum_parent}")
