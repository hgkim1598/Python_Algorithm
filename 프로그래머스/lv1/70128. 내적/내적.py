def solution(a, b):
    answer = 0
    list = []
    for i in range(len(a)):
        list.append(a[i] * b[i])
        
    answer = sum(list)
    return answer