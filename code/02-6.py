import sys

sys.stdin = open("sample_input.txt", "r")

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(A)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    subsets = []
    for i in range(1 << n):  # 1<<n = 1000000(64) => 부분 집합의 개수
        subset = []
        for j in range(n):  # 원소의 수만큼 비트를 비교 => 원소의 포함 여부 판단이 가능함
            if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
                subset.append(A[j])
        if len(subset) == N:
            subsets.append(subset)

    count = 0
    for subset in subsets:
        if sum(subset) == K:
            count += 1

    print(f"#{test_case} {count}")
