def encoding(unit, s):
    count = 1
    enc_s = ""
    for idx in range(0, len(s), unit):
        if idx + unit <= len(s): 
            unit_s = s[idx:idx+unit]
            if unit_s == s[idx+unit:idx+2*unit]:
                count += 1
            else:
                if count == 1:
                    enc_s += unit_s
                else:   
                    enc_s += f"{count}{unit_s}"
                    count = 1
        elif idx + unit > len(s):
            enc_s += s[idx:]

    print(enc_s)
    return enc_s
        

def solution(s):
    min_len = 1001

    if len(s) > 1:
        for unit in range(1, len(s)//2 + 1):
            len_s = len(encoding(unit, s))
            min_len = min(min_len, len_s)
    else:
        min_len = 1

    print(min_len)
    return min_len

solution("a")