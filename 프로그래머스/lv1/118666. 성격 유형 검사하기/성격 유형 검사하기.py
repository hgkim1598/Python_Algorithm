def solution(survey, choices):
    answer = ''
    type_list = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    type_dict = {key: 0 for key in type_list}
    
    for i in range(len(survey)):
            if choices[i] < 4:
                if survey[i][0] in type_dict:
                    type_dict[survey[i][0]] += (4 - choices[i])
            elif choices[i] > 4:
                if survey[i][1] in type_dict:
                    type_dict[survey[i][1]] += (choices[i] - 4)
            else:
                continue
    
    # type_dict_keys = list(type_dict.keys())
    for idx, key in enumerate(type_list):
        if idx % 2 == 0:
            cur_val = type_dict[key]
            next_val = type_dict[type_list[idx+1]]
            if cur_val > next_val:
                answer += key
            elif cur_val < next_val:
                answer += type_list[idx+1]
            else: 
                answer += key
                    
    return answer