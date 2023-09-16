def solution(N, stages):
    answer = []
    failure = {}
    
    for i in range(1, N+1):
        reach = 0
        yet = 0
        for j in stages:
            if j >= i:
                reach += 1
            if j == i:
                yet += 1
        if yet == 0:
            failure[i] = 0
        else:
            failure[i] = yet / reach
        
    sorted_fail = dict(sorted(failure.items(), key=lambda item: item[1], reverse=True))
    answer = list(sorted_fail.keys())
    return answer