def solution(n):
    answer = []
    str_n = str(n)
    for i in str_n:
        answer.append(int(i))
    answer.reverse()
    return answer
# n을 문자열로 만들고
# for문을 돌면서
# int() -> answer에 append
# .reverse()