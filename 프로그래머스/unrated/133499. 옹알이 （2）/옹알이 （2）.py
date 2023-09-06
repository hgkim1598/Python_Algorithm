def solution(babbling):
    answer = 0
    pron = ['aya', 'ye', 'woo', 'ma']
    answer_list = []
    say = ''
    pre_say = ''
    for i in range(len(babbling)):
        for j in range(len(babbling[i])):
            say += babbling[i][j]
            if say in pron:
                if say != pre_say:
                    pre_say = say
                    say = ''
                else:
                    break
        if say == '':
            answer_list.append(babbling[i])
            pre_say =''
        else:
            say = ''
            pre_say = ''
    
    answer = len(answer_list)
    return answer