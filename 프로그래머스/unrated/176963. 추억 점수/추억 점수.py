def solution(name, yearning, photo):
    answer = []
    missing = dict(zip(name, yearning))
    
    for i in photo:
        miss_sum = 0
        for j in i:
            if j in missing:
                miss_sum += missing[j]
            else:
                miss_sum += 0
        answer.append(miss_sum)
        
    return answer