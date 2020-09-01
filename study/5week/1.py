# 패턴 마디의 길이

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


def findWord(string):

    for idx, char in enumerate(string):
        if idx == 0:
            first = char
        else:
            if char == first and char == string[idx*2]:
                return idx


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    string = input()

    answer = findWord(string)

    print(f'#{test_case} {answer}')
