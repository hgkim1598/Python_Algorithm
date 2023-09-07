def solution(k, m, score):
    answer = 0
    p = 0
    score = sorted(score, reverse = True)
    i = 0
    while i <= len(score)-m:
        p = min(score[i:i+m])
        answer += p*m
        i += m
    return answer