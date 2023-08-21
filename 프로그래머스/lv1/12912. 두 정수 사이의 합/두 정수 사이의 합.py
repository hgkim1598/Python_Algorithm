def solution(a, b):
    # 두 수가 같은 경우 먼저 걸러내기 (if 같다면~)
    # sum과 range 사용 (마지막 포함)
    
    answer = 0
    if a == b:
        return a
    if a < b:
        answer = sum(range(a, b+1))
    else:
        answer = sum(range(b, a+1))
    return answer