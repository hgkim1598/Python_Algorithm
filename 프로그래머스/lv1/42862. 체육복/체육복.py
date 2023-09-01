def solution(n, lost, reserve):
    answer = 0
    pe_uni = []
    # 도난 이후 학생들 체육복 현황
    pe_uni = [1] * n
    for i in range(len(lost)):
        pe_uni[lost[i]-1] -= 1
    for i in range(len(reserve)):
        pe_uni[reserve[i]-1] += 1
    
    # 체육복 빌려주기
    if pe_uni[0] == 0:
        if pe_uni[1] == 2:
            pe_uni[1] -= 1
            pe_uni[0] += 1
    if pe_uni[n-1] == 0:
        if pe_uni[n-2] == 2:
            pe_uni[n-2] -= 1
            pe_uni[n-1] += 1
    for i in range(1, n-1):
        if pe_uni[i] == 0:
            if pe_uni[i-1] == 2:
                pe_uni[i-1] -= 1
                pe_uni[i] += 1
            elif pe_uni[i+1] == 2:
                pe_uni[i+1] -= 1
                pe_uni[i] += 1
    
    # 수업을 들을 수 있는 학생들
    for i in range(n):
        if pe_uni[i] != 0:
            answer += 1
    
    return answer