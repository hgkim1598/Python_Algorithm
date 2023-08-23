def solution(n):
    answer = '수'
    for i in range(1, n):
        if answer[-1] == '수':
            answer += '박'
        else:
            answer += '수'
    return answer
# 우선 '수'로 시작 -> 빈문자열로 초기화 하는 걸로 바꿔봄
# for문을 돌면서 answer의 마지막이 '수'이면 '박'을 붙이고, '박'이면 '수'를 붙임
# 생각해보니 무조건 수 아니면 박이라 굳이 조건을 두 개 검사하지 않고 else로..!
# 범위 = range(1, n+1)? range(1, n)?
