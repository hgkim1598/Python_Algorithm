def solution(seoul):
    kim_idx = seoul.index("Kim")
    return f'김서방은 {kim_idx}에 있다'
# index 반환 받는 법: index(찾고자 하는 요소)
# 처음에 for문을 돌려고 했는데 위 메서드를 사용하면 for문 돌지 않아도 됨