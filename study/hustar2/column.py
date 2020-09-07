# 카카오 2020 기출 / 기둥과 보

# 규칙
# 기둥 : 바닥 위 or 보의 한쪽 끝 부분 위 or 다른 기둥 위
# 보 : 한쪽 끝 부분이 기둥 위 or 양쪽 끝 부분이 다른 보와 연결

def add_row(x, y, mat, n):
    if x == 0:
        if (mat[y-1][x] in (0, 2)) or (mat[y-1][x+1] in (0, 2)):
            return True
    else:
        if (mat[y-1][x] in (0, 2)) or (mat[y-1][x+1] in (0, 2)) or (mat[y][x-1] in (1, 2) and mat[y][x+1] in (1, 2)):
            return True
    return False


def add_column(x, y, mat, n):
    if y == 0:
        return True
    if x == 0:
        if (mat[y-1][x] in (0, 2)) or (mat[y][x] == 1):
            return True
    else:
        if (mat[y-1][x] in (0, 2)) or (mat[y][x-1] in (1, 2)) or (mat[y][x] == 1):
            return True
    return False


def solution(n, build_frame):
    answer = []

    # -1 : 없음, 0: 기둥, 1: 보, 2: 둘 다
    mat = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    # a = 0: 기둥, 1: 보 / b = 0: 삭제, 1: 설치
    for x, y, a, b in build_frame:
        if b:  # 설치
            if a:  # 보
                if add_row(x, y, mat, n):
                    mat[y][x] += 2
                    answer.append([x, y, a])
                    continue
            else:  # 기둥
                if add_column(x, y, mat, n):
                    mat[y][x] += 1
                    answer.append([x, y, a])
                    continue
        else:  # 삭제
            if a:  # 보
                mat[y][x] -= 2
                # 삭제할 보 위에 기둥이 있는 경우
                if mat[y][x] == 0:
                    if not add_column(x, y, mat, n):
                        mat[y][x] += 2
                        continue
                if mat[y][x+1] == 0:
                    if not add_column(x+1, y, mat, n):
                        mat[y][x] += 2
                        continue
                # 삭제할 보 양 옆에 보가 있는 경우
                if x >= 2 and mat[y][x-1] in (1, 2):
                    if not add_row(x-1, y, mat, n):
                        mat[y][x] += 2
                        continue
                if x <= n-3 and mat[y][x+1] in (1, 2):
                    if not add_row(x+1, y, mat, n):
                        mat[y][x] += 2
                        continue
            else:  # 기둥
                mat[y][x] -= 1
                # 삭제할 기둥 위에 기둥이 있는 경우
                if y < n-1 and mat[y+1][x] == 0:
                    if not add_column(x, y+1, mat, n):
                        mat[y][x] += 1
                        continue
                # 삭제할 기둥 위에 보가 있는 경우
                if x < n and mat[y+1][x] in (1, 2):
                    if not add_row(x, y+1, mat, n):
                        mat[y][x] += 1
                        continue
                if x > 0 and mat[y+1][x-1] in (1, 2):
                    if not add_row(x-1, y+1, mat, n):
                        mat[y][x] += 1
                        continue
            answer.remove([x, y, a])

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
      1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
