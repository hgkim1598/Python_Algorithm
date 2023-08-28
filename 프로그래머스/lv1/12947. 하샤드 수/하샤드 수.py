def solution(x):
    num = 0
    x_to_str = str(x)
    for i in x_to_str:
        num += int(i)
    if x % num == 0:
        answer = True
    else:
        answer = False
    return answer