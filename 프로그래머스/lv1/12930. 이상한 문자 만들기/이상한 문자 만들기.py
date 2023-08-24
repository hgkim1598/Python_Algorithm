def solution(s):
    answer = ''
    words = s.split(' ')
    for i in words:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "
    return answer[0:-1]
# 대소문자 변경
# 단어 내에서 for문을 돌면서
# i.index() % 2 == 0이면 i.upper() -> .index() 활용 불가라고 한다?! 문자열의 각 문자에는 인덱스가 없다고,,
# 아니라면 i.lower()
# answer에 더해주기

# 단어 구분
# split(' ')

# 마지막에 붙은 공백을 지워주는 게 관건!