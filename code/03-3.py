import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    pattern = input()
    text = input()

    len_p = len(pattern)
    len_t = len(text)
    idx_p = 0
    idx_t = len_p - 1

    skip = {}
    for i, s in enumerate(pattern):
        skip[s] = len_p - 1 - i
    # skip 배열 : pattern 존재하면 - len_p - 1 - i / 없는 문자면 len_p

    while idx_p < len_p and idx_t < len_t:
        for s in pattern[::-1]:
            if s == text[idx_t]:
                idx_t -= 1
                idx_p += 1
            else:
                try:
                    idx_t += skip[text[idx_t]]
                except:
                    idx_t += len_p
                idx_p = 0
                break

    if idx_p == len_p:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
