# 암호 생성기
from queue import Queue
import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(10):

    T = int(input())
    nums = [num for num in map(int, input().split())]
    cycles, remain = divmod(min(nums), 15)
    if remain == 0:
        cycles -= 1
    password = Queue(8)

    for num in nums:
        password.put(num - (15 * cycles))

    is_continue = True
    i = 1

    while is_continue:
        first = password.get()
        new = first - i
        if new <= 0:
            is_continue = False
        password.put(max(new, 0))
        i = 1 if i == 5 else i + 1

    print(f"#{T}", end=' ')
    for _ in range(8):
        print(password.get(), end=' ')
    print()
