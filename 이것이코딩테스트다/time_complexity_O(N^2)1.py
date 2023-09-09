### 2중 반복문을 이용하는 프로그램 예제

array = [3, 5, 1, 2, 4]  # 5개의 데이터 (N = 5)

for i in array:
    for j in array:
        temp = i * j
        print(temp)
        
# 시간 복잡도: O(N^2)