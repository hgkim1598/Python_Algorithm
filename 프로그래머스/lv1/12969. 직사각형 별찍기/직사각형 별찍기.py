a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end='')
    if i != b-1:
        print()
# 주어진 함수 = 들어온 숫자 두 개를 각각 나누는 함수 -> a, b로