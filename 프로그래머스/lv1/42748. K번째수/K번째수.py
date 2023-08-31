def solution(array, commands):
    answer = []
    for a in commands:
        i, j, k = a
        arr = array[i-1: j]
        sort_arr = sorted(arr)
        answer.append(sort_arr[k-1])
    return answer