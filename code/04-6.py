import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())

    Memo = [1, 3]

    for i in range(N//10 - 2):
        Memo.append(Memo[i]*2 + Memo[i+1])

    print(f"#{test_case} {Memo[-1]}")
