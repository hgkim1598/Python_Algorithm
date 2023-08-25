def solution(n):
    answer = 0
    x = n**0.5
    if x.is_integer() == True and x > 0:
        answer = (x+1)**2
    else:
        answer = -1
    return answer
# 제곱근 구하는 함수? -> **0.5
# x = n**0.5
# 양의 정수의 제곱일 경우 -> .is_integer() and > 0
# (x+1)**2

# 양의 정수의 제곱이 아닐 경우 -> else
# answer = -1
