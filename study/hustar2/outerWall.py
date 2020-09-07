# 외벽 점검 - 카카오 2020 공채

def solution(n, weak, dist):

    m = len(weak)
    interval = m - 1

    friend = dist.pop()
    candi = []

    while True:
        for i in range(m):
            dst = (i + interval) % m
            st = i % m
            sub = weak[dst] - weak[st]
            if i + interval >= m:
                sub += 12
            if friend >= sub:
                candi.append((st, dst))
        if candi != []:
            break

        interval -= 1
        if interval == 0:
            if len(weak) > len(dist):
                return -1
            break

    visit_count = interval + 1
    if visit_count == m:
        return 1
    if visit_count == m - 1:
        return 2
    if visit_count <= m - 2:
        min_friends = 9
        for st, dst in candi:
            weak_temp = weak[::]
            dist_temp = dist[::]
            if st < dst:
                for n in range(dst, st-1, -1):
                    weak_temp.pop(n)
            elif st > dst:
                for n in range(m-st):
                    weak_temp.pop()
                for n in range(dst, -1, -1):
                    weak_temp.pop(n)
            res = solution(n, weak_temp, dist_temp)
            if res == -1:
                continue
            min_friends = min(res, min_friends)
        if min_friends == 9:
            return -1
        return 1 + min_friends

    return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
