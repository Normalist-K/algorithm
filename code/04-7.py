import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    text = input()

    stack = []

    isFalse = 0

    for s in text:
        if s == "[" or s == "{" or s == "(":
            stack.append(s)
        elif s == "]" or s == "}" or s == ")":
            if len(stack) == 0:
                print(f"#{test_case} 0")
                isFalse = 1
                break
            else:
                compare = stack.pop()
                if (s == "]" and compare == "[") or (s == "}" and compare == "{") or (s == ")" and compare == "("):
                    continue
                else:
                    print(f"#{test_case} 0")
                    isFalse = 1
                    break

    if isFalse == 0:
        if len(stack) != 0:
            print(f"#{test_case} 0")
        else:
            print(f"#{test_case} 1")
