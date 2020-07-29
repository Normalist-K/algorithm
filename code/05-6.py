import sys

sys.stdin = open("sample_input.txt", "r")

# 가위 바위 보


def game(students, i, j):
    if (students[i - 1][1] == 1 and students[j - 1][1] == 2) or (students[i - 1][1] == 2 and students[j - 1][1] == 3) or (students[i - 1][1] == 3 and students[j - 1][1] == 1):
        return j
    else:
        return i

# 반으로 나누고 승자를 구하는 함수


def divide_win(students, i, j):
    if j - i == 1:
        return game(students, i, j)
    elif i == j:
        return i
    else:
        nj = (i + j) // 2
        ni = nj + 1
        return game(students, divide_win(students, i, nj), divide_win(students, ni, j))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    # 인원수, (학생 번호, 카드) 입력받기
    N = int(input())
    students = [(idx+1, int(card)) for idx, card in enumerate(input().split())]

    winner = divide_win(students, 1, N)

    print(f"#{test_case} {students[winner - 1][0]}")
