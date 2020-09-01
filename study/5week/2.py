# 성공적인 공연 기획

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


def hire(string):
    hired = 0
    clap = 0
    for need, char in enumerate(string):
        num = int(char)
        if need == 0:
            clap = num
        else:
            if num != 0:
                if clap >= need:
                    clap += num
                else:
                    hire_now = need - clap
                    hired += hire_now
                    clap += hire_now + num

    return hired


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    string = input()

    answer = hire(string)

    print(f'#{test_case} {answer}')
