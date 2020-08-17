import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


def sum_children(list_node, N, index_node):
    if index_node * 2 > N:
        return list_node[index_node]

    child_left = sum_children(list_node, N, index_node * 2)
    child_right = 0 if (
        index_node * 2 + 1) > N else sum_children(list_node, N, index_node * 2 + 1)
    list_node[index_node] = child_left + child_right

    return list_node[index_node]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M, L = map(int, input().split())

    list_node = [0 for _ in range(N)]
    list_node = [None] + list_node

    for _ in range(M):
        idx, value = map(int, input().split())
        list_node[idx] = value

    print(f"#{test_case} {sum_children(list_node, N, L)}")
