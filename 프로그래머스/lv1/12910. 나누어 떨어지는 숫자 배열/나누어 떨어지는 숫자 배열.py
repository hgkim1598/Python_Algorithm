def solution(arr, divisor):
    # arr내 값을 돌면서 divisor로 나눈 나머지가 0인 요소를 answer에 append
    # if 문을 사용하고 else answer에 아무 것도 없다면 return -1
    #  => if else가 아니라 각각 다른 if 문으로..!
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer