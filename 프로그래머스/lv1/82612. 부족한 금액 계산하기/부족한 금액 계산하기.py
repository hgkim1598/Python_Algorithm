def solution(price, money, count):
    answer = 0
    rest = money
    for i in range(1, count+1):
        rest = rest - price*i
    
    if rest < 0:
        answer = rest*(-1)
    else:
        answer = 0
    return answer