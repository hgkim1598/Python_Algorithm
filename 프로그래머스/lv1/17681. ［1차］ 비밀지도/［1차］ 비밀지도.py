def to_bin(arr, n):
    bin_matrix = []
    for i in arr:
        n_to_bin = bin(i)[2:].zfill(n)
        bin_list = []
        for j in n_to_bin:
            bin_list.append(int(j))
        bin_matrix.append(bin_list)
    return bin_matrix

def wall_or_empty(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                arr[i][j] = '#'
            else:
                arr[i][j] = ' '
    return arr

def solution(n, arr1, arr2):
    answer = []
    bin_mat_1 = to_bin(arr1, n)
    bin_mat_2 = to_bin(arr2, n)
    woe_1 = wall_or_empty(bin_mat_1)
    woe_2 = wall_or_empty(bin_mat_2)
    for i in range(n):
        temp = ''
        for j in range(n):
            if woe_1[i][j] == ' ' and woe_2[i][j] == ' ':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer