import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    string = input()
    stack = []

    for s in string:
        if len(stack) == 0:
            stack.append(s)
        else:
            if s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)

    print(f"#{test_case} {len(stack)}")
