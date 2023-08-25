def solution(n):
    answer = 0
    list_n = []
    str_n = str(n)
    sorted_n = ''.join(sorted(str_n, reverse=True))
    answer = int(sorted_n)
    return answer
# 숫자 -> 문자열 -> 리스트 -> 내림차순 -> 문자열 -> 숫자
# 생각 나는 방법은 이것 뿐인데 이게 과연 효율적인가?
# 리스트 -> 문자열 부분이 X
# 문자열에도 sorted()를 사용할 수 있다 기억하기!