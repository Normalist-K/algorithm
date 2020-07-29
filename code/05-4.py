import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    postfix = list(input().split())
    stack = []

    for s in postfix:
        if s in ('+', '-', '*', '/'):
            if len(stack) >= 2:
                second = stack.pop()
                first = stack.pop()
                if s is '+':
                    result = first + second
                if s is '-':
                    result = first - second
                if s is '*':
                    result = first * second
                if s is '/':
                    result = first // second
                stack.append(result)
            else:
                print(f"#{test_case} error")
                break
        elif s == '.':
            if len(stack) == 1:
                print(f"#{test_case} {stack.pop()}")
            else:
                print(f"#{test_case} error")
                break
        else:
            stack.append(int(s))
