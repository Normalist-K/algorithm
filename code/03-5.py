import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    str1 = input()
    str2 = input()

    # str1을 dict로 바꿔서 중복되는 문자 제거
    dict1 = {}
    for s in str1:
        dict1[s] = 0

    # str2 for문 돌면서 dict1 key와 같으면 value 1 증가
    for s in str2:
        if s in dict1:
            dict1[s] += 1

    max_s = max(dict1.values())

    print(f"#{test_case} {max_s}")
