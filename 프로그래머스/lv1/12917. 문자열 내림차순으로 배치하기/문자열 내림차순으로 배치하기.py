def solution(s):
    answer = ''
    descending = sorted(s, reverse = True)
    
    answer = ''.join(descending)
    return answer