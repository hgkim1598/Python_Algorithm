def solution(x, n):
    answer = []
    for i in range(n):
        num = x + i*x
        answer.append(num)
    return answer