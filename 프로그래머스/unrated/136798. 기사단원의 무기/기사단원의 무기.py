def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        divisor = 0
        for j in range(1, int(i**0.5)+1):  # 1 ~ 제곱근 수 까지
            if i % j == 0:  # 만약 i가 j로 나누어떨어지면서
                if j ** 2 == i:  # j가 i의 제곱근이면
                    divisor += 1  # 한 번만 count (ex. 3*3 = 9, 3은 한 번만 count)
                else:  # 그 외의 약수의 경우는
                    divisor += 2  # 짝을 이루는 수 까지 한 번에 더하기
        if divisor > limit:  # 만약 i에 대한 약수 개수가 limit보다 크면
            divisor = power  # 약수 개수 대신 power를!
        answer += divisor  # i에 대한 결과를 그때 그때 더해줌
    return answer