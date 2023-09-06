def solution(food):
    answer = ''
    left_par = ''
    for i in range(1, len(food)):
        how_many = food[i] // 2
        left_par += str(i)*how_many
    answer = left_par + '0'*food[0] + left_par[::-1]
    return answer