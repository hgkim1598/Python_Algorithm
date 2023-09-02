def ranking(num):
    rate = 0
    list = [6, 5, 4, 3, 2]
    for i in range(len(list)):
        if list[i] == num:
            rate = i+1
    if num <= 1:
        rate = 6
    return rate

def solution(lottos, win_nums):
    answer = []
    # 채점할 수 있는 것 먼저
    same = 0
    for i in range(len(lottos)):
        if lottos[i] != 0:
            if lottos[i] in win_nums:
                same += 1
    
    # 최고 점수
    top_count = same + lottos.count(0)
    
    # 최저 점수
    low_count = same
    
    top_rank = ranking(top_count)
    low_rank = ranking(low_count)
    
    # answer
    answer.append(top_rank)
    answer.append(low_rank)
    return answer