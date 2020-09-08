# 외벽 점검 - 카카오 2020 공채

def solution(n, weak, dist):

    m = len(weak)

    if m == 1 and len(dist) >= 1:
        return 1

    interval = m - 1

    if len(dist) == 0:
        return -1

    friend = dist.pop()
    candi = []

    while True:
        for i in range(m):
            dst = (i + interval) % m
            st = i % m
            sub = weak[dst] - weak[st]
            if i + interval >= m:
                sub += n
            if friend >= sub:
                next_comp = (dst + 1) % m
                if next_comp < st:
                    sub_comp = weak[next_comp] - weak[dst]
                    if dst + 1 >= m:
                        sub_comp += n
                    if friend - sub >= sub_comp:
                        continue
                candi.append((st, dst, interval+1))

        interval -= 1
        if interval == 0:
            if candi == []:
                if len(weak) <= len(dist):
                    return len(weak)
                else:
                    return -1
            break

    print(candi)

    min_friends = 9
    for st, dst, visit_count in candi:
        if visit_count == m:
            return 1
        if visit_count == m - 1 and len(dist) >= 1:
            return 2
        if visit_count <= m - 2:
            weak_temp = weak[::]
            dist_temp = dist[::]
            if st < dst:
                for idx in range(dst, st-1, -1):
                    weak_temp.pop(idx)
            elif st > dst:
                for idx in range(m-st):
                    weak_temp.pop()
                for idx in range(dst, -1, -1):
                    weak_temp.pop(idx)
            res = solution(n, weak_temp, dist_temp)
            if res == -1:
                continue
            min_friends = min(res, min_friends)

    if min_friends == 9:
        return -1
    return 1 + min_friends


print(solution(100, [0, 10], [3, 5, 7]))
