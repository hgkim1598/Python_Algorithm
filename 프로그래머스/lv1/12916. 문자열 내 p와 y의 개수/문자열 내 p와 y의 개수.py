def solution(s):
    answer = True
    p = y = 0
    for i in s:
        if (i == 'p' or i == 'P'):
            p += 1
        elif (i == 'y' or i == 'Y'):
            y += 1
    if p == y:
        answer = True
    else:
        answer = False
    return answer
# for문을 돌면서 s 내의 요소들 하나씩 확인
# i == p or i == P 인 경우 m += 1
# i == y or i == Y 인 경우 n += 1
# if m == n == 0이면 answer는 true
# if m == n이면 answer는 true, else면 false