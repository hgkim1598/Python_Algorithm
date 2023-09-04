def solution(a, b, n):
    total_coke = 0  # 상빈이가 전체적으로 받을 수 있는 콜라의 양

    while n >= a:  # 빈 병이 a개 이상인 동안
        # a개의 빈 병으로 b병의 콜라를 받을 수 있음
        exchanged_coke = (n // a) * b
        total_coke += exchanged_coke

        # 남아있는 빈 병 + 새롭게 마시게 될 콜라 병의 개수로 n 업데이트
        n = n - (n // a) * a + exchanged_coke

    return total_coke

