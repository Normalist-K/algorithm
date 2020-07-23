import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    P, A, B = map(int, input().split())

    A_start = 1
    A_end = P
    A_count = 0
    B_start = 1
    B_end = P
    B_count = 0

    while A_start <= A_end:

        A_count += 1
        middle = int((A_start + A_end)/2)

        if A == middle:
            break
        elif A < middle:
            A_end = middle
        else:
            A_start = middle

    while B_start <= B_end:

        B_count += 1
        middle = int((B_start + B_end)/2)

        if B == middle:
            break
        elif B < middle:
            B_end = middle
        else:
            B_start = middle

    if A_count < B_count:
        result = "A"
    elif A_count > B_count:
        result = "B"
    else:
        result = 0

    print(f"#{test_case} {result}")
