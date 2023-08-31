def solution(answers):
    answer = []
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(len(answers)):
        if answers[i] == supo_1[i%5]:
            s1 += 1
        if answers[i] == supo_2[i%8]:
            s2 += 1
        if answers[i] == supo_3[i%10]:
            s3 += 1
            
    top_score = max(s1, s2, s3)
    if top_score == s1:
        answer.append(1)
    if top_score == s2:
        answer.append(2)
    if top_score == s3:
        answer.append(3)
    return answer