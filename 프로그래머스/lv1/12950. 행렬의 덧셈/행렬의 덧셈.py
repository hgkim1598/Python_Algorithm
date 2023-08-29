def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        each_row = []
        for j in range(len(arr1[i])):
            each_row.append(arr1[i][j] + arr2[i][j])
        answer.append(each_row)
    return answer
# len(행렬명) 하면 행렬의 행 개수를 반환한다
# arr1과 arr2의 행과 열의 길이는 같으므로 for문에 어떤 행렬을 넣어도 상관 없을 듯
# 빈 배열에 행 하나에 대한 덧셈 결과값들을 넣고 붙이고의 반복