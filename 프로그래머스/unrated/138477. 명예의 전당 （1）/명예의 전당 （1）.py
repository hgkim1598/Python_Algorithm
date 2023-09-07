def solution(k, score):
    answer = []
    fame = []
    for i in range(len(score)):
        if i <= k-1:
            fame.append(score[i])
        else:
            if min(fame) < score[i]:
                idx = fame.index(min(fame))
                fame[idx] = score[i]
        answer.append(min(fame))
    return answer