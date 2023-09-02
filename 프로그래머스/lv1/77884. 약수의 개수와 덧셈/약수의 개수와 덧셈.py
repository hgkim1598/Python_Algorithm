def devided(num):
    devisor = []
    for i in range(1, num+1):
        if num % i == 0:
            devisor.append(i)
    return len(devisor)

def solution(left, right):
    answer = 0
    sum_list = []
    for i in range(left, right+1):
        if devided(i) % 2 == 0:
            sum_list.append(i)
        else:
            sum_list.append(i*(-1))
    answer = sum(sum_list)
    return answer