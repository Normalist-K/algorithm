# 간단한 369게임

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())

    for num in range(1, N+1):
        if '3' in str(num) or '6' in str(num) or '9' in str(num):
            for char in str(num):
                if char in ('3', '6', '9'):
                    print('-', end='')
            print(' ', end='')
        else:
            print(num, end=' ')

    print()
