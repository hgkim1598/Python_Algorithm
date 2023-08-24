def solution(n):
    answer = 0
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    answer = sum(divisor)
    return answer
# 약수 구하기
# 1. range(1, n+1)의 범위로 for문을 돌면서
# 2. n % i == 0 이 되면 약수 리스트에 append
# 혹시 for문 없이 구하는 방법도 있나?

# for문 돌면서 하나씩 더하지 말고
# sum 함수 활용해보기