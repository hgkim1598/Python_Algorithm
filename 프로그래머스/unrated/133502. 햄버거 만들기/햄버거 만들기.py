def solution(ingredient):
    answer = 0
    berger =[]
    hamberger = [1, 2, 3, 1]
    for i in ingredient:
        berger.append(i)
        if berger[-4:] == hamberger:
            answer += 1
            for j in range(4):
                berger.pop()

    return answer