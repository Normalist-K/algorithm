def chk(u):
    stack = []
    for s in u:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack == []:
                return False
            stack.pop()
    return True

def solution(p):
    
    if p == '':
        answer = ''

    chk_count = 0
    idx = 0

    for idx, bracket in enumerate(p):
        if bracket == '(':
            chk_count += 1
        elif bracket == ')':
            chk_count -= 1
        
        if chk_count == 0:
            break

    u, v = p[:idx+1], p[idx+1:]
    new_v = solution(v)

    if chk(u):
        u += new_v
    else:
        answer = '('
        answer += (new_v + ')')
        if len(u) > 2:
            answer += u[1:len(u)-1:-1]
        
    print(answer)
    return answer

solution("(()())()")