def solution(phone_number):
    ph_lst = list(phone_number)
    for i in range((len(ph_lst)-4)):
        ph_lst[i] = '*'
    return ''.join(ph_lst)