def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    min_num = min(arr)
    for i in arr:
        if i == min_num:
            continue
        else:
            answer.append(i)
    return answer
# 가장 작은 수 찾기
# for문을 돌면서
# min = arr[0]
# arr[i] < min 일 경우 min = arr[i]

# 가장 작은 수를 제외한 배열 만들기
# for문을 돌면서 answer에 추가하는데
# 만약 min과 같은 수가 나오면 continue