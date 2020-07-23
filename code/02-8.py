import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(10):
        max_idx = i
        min_idx = i
        if i % 2 == 0:
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[max_idx]:
                    max_idx = j
            nums[i], nums[max_idx] = nums[max_idx], nums[i]
        else:
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    print(f"#{test_case}", end=' ')
    for i in nums[:10]:
        print(f"{i}", end=' ')
    print('')
