def solution(s, skip, index):
    answer = ''
    alp_low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alp_lst = []
    for i in alp_low:
        if i not in skip:
            alp_lst.append(i)
    
    for i in s:
        i_idx = alp_lst.index(i)
        answer += alp_lst[(i_idx + index) % len(alp_lst)]
    return answer