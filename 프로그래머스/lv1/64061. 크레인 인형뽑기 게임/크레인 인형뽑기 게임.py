def solution(board, moves):
    answer = 0
    bascket = []
    # 인형 뽑기
    for i in moves:
        for j in board:
            if j[i-1] == 0:
                continue
            else:
                bascket.append(j[i-1])
                j[i-1] = 0
                break
                
    # 인형 터트리기
    while True:
        removed = False
        i = 0
        while i < len(bascket) - 1:
            if bascket[i] == bascket[i+1]:
                bascket.pop(i)
                bascket.pop(i)
                answer += 2
                removed = True
                break
            i += 1
        if not removed:
            break
        
    return answer