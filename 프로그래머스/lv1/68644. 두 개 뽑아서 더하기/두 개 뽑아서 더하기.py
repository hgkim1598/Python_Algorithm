def solution(numbers):
    answer = []
    sum_list = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum_list.append(numbers[i] + numbers[j])
    unique_list = set(sum_list)
    answer = sorted(unique_list)
    return answer