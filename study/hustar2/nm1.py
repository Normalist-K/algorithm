# N과 M 1
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


def NM(nums, visited, depth, M):
    if depth == M:
        print(visited)
        visited = []
    else:
        for num in nums:
            if num not in visited:
                visited.append(nu
                NM(nums, visited, depth+1, M)


T=int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M=map(int, input().split())
    nums=[num for num in range(1, N+1)]
    visited=[]

    NM(nums, visited, 0, M)
