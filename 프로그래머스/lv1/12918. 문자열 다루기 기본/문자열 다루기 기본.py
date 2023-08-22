def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        if s.isdecimal():
            answer = True
        else:
            answer = False
    else:
        answer = False
    return answer
# 조건 1: s의 길이가 4 혹은 6 인지 아닌지
# 조건 2: 숫자로만 구성되어 있는지
# 조건 1과 2를 모두 만족하는 경우에 True
# 아닌 경우 전부 False
# 숫자 list를 만들려다가 is...가 생각이 났다 => isdecimal!