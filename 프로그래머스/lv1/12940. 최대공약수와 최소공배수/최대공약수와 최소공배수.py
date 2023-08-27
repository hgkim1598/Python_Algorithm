import math
def solution(n, m):
    answer = []
    gcd_num = math.gcd(n,m)
    answer.append(gcd_num)
    lcm_num = (n*m)/gcd_num
    answer.append(lcm_num)
    return answer
# 최대 공약수 구하기
# mat 라이브러리 gcd 함수
# 최소 공배수 구하기
# 두 수를 곱한 결과를 최대 공약수로 나눔