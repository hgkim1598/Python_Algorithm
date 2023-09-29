def solution(today, terms, privacies):
    answer = []
    terms_dic = {t[0]: int(t[2:]) * 28 for t in terms}

    today = list(map(int, today.split('.')))
    today = today[0] * 12 * 28 + today[1] * 28 + today[2] 
    for idx in range(len(privacies)):
        day, code = privacies[idx].split(' ')  
        day = list(map(int, day.split('.')))
        day = day[0] * 12 * 28 + day[1] * 28 + day[2]  
        if day + terms_dic[code] <= today:
            answer.append(idx + 1)

    return answer