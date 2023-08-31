def solution(participant, completion):
    answer = ''
    parti = sorted(participant)
    compl = sorted(completion) 
    for i in range(len(compl)):
        if parti[i] != compl[i]:
            return parti[i]
    return parti[-1]