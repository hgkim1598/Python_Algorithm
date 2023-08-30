from itertools import combinations
def is_prime_num(n):
    p_num = []
    for i in range(1, n+1):
        if n % i == 0:
            p_num.append(i)
    return len(p_num) == 2

def solution(nums):
    answer = 0
    comb = []
    
    comb = combinations(nums,3)
    
    for i in comb:
        if is_prime_num(sum(i)):
            answer += 1

    return answer