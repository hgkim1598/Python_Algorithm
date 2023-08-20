def solution(arr):
    # 빈 리스트를 만들고 arr에서 0번째부터 append해줌
    # 1번이 0번과 같지 않다면 append, 같다면 append하지 않음
    # 나머지도 i-1번과 i가 같지 않다면 append
    
    answer = []
    answer.append(arr[0])  # 일단 첫 번째 숫자 append
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer