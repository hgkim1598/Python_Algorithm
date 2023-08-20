def solution(s):
    # 홀수면 len(s)//2번째, 짝수면 len(s)//2-1, (len(s)//2)번째
    middle = int(len(s)//2)
    if len(s) % 2 == 0:
        answer = s[middle-1:middle+1]
    else:
        answer = s[middle]
    return answer