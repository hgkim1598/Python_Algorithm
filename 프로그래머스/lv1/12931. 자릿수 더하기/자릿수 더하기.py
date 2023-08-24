def solution(n):
    answer = 0
    num_to_str = str(n)
    int_li = [int(i) for i in num_to_str]
    answer = sum(int_li)

    return answer
# 문자열로 바꿔서(str()) 각각을 요소로 만들고 그걸 리스트로 만들고(list())
# 각 요소에 int()를 적용해서 sum 해준다면?

# 문자열도 순회 가능하므로 굳이 리스트로 만들 필요 x?