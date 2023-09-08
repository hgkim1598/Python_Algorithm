def solution(t, p):
    answer = 0
    a = ''
    for i in range(len(t)-len(p)+1):
        a += t[i:i+len(p)]
        if int(a) <= int(p):
            answer += 1
        a = ''
    return answer