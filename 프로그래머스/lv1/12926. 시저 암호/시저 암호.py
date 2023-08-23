def solution(s, n):
    answer = ''
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in s:
        if i.isupper() == True:
            idx = upper.index(i)
            caesar = idx + n
            if caesar > 25:
                caesar -= 26
            answer += upper[caesar]
        elif i.islower() == True:
            idx = lower.index(i)
            caesar = idx + n
            if caesar > 25:
                caesar -= 26
            answer += lower[caesar]
        else:
            answer += ' '
    return answer
# 대문자 리스트, 소문자 리스트/문자열 생성? -> 이것 때문에 런타임 에러 나는 듯?
# for문 돌면서
# 공백은 공백으로 처리
# 1. s의 i번째 요소가 대문자인지 소문자인지 판별 -> isupper() -> True면 대문자 리스트에서
# 2. 해당 리스트에서 i가 몇 번째 요소인지 확인
# 3. 2번에서 찾은 인덱스 +n 해준 결과를 반환

# z -> a 어떻게??
# 알파벳 26개 -> index 25번에서 끝남
# ceasar가 25를 넘어갈 경우 ceasar - 26 해주기 (ex. ceasar가 26일 경우 0인 a로 가야함)

# 반복되는 구문 따로 빼서 함수로 만드는 방법도 생각해보기