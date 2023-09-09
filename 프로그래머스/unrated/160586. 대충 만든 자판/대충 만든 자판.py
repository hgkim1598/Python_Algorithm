def solution(keymap, targets):
    answer = []

    for target in targets:
        count = 0
        not_found = False  # 플래그 설정
        
        for char in target:
            min_idx = 101
            for k in keymap:
                if char in k:
                    idx = k.index(char)
                    min_idx = min(min_idx, idx)
            if min_idx == 101:  # 문자를 찾지 못한 경우
                not_found = True
                break
            count += (min_idx + 1)

        if not_found:
            answer.append(-1)
        else:
            answer.append(count)

    return answer
