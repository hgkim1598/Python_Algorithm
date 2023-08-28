def solution(num):
    count = 0
    if num == 1:
        count = 0
    while num != 1:
        if count >= 500:
            return -1
        if num % 2 == 0:
            num = num/2
        else:
            num = num * 3 + 1
        count += 1
    return count
# while문 계속 돌면서
# 들어온 수가 짝수라면 ~
# num = num/2
# 들어온 수가 홀수라면 ~
# num = num * 3 + 1