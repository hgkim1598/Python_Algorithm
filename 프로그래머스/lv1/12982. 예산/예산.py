def solution(d, budget):
    answer = 0
    if sum(d) <= budget:
        answer = len(d)
    else:
        req_sum = 0
        sorted_d = sorted(d)
        for i in sorted_d:
            req_sum += i
            if req_sum > budget:
                break
            else:
                answer += 1
            
    return answer