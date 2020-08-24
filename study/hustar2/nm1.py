# N과 M 1
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


def perm(lst, n):
    ret = []

    if n > len(lst):
        return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in perm(temp, n-1):
                ret.append([lst[i]] + p)

    return ret


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    nums = [num for num in range(1, N+1)]
    visited = [False for _ in range(N+1)]

    print(perm(nums, M))
