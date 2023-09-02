def solution(absolutes, signs):
    answer = 0
    ans_list = []
    for i in range(len(signs)):
        if signs[i] == True:
            ans_list.append(absolutes[i] * 1)
        else:
            ans_list.append(absolutes[i] * (-1))
    answer = sum(ans_list)
    return answer