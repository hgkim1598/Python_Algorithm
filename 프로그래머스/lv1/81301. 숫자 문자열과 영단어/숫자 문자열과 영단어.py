def solution(s):
    answer = 0
    word_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    answer_str = ''
    word = ''
    for i in s:
        if i.isdigit() == True:
            answer_str += i
        else:
            word += i
            if word in word_dict:
                answer_str += word_dict[word]
                word = ''  # 다음 단어 검사를 위해 word 비워주기
            else:
                continue
    answer = int(answer_str)
                
    return answer