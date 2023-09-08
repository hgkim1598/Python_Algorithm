def solution(s):
    answer = []
    spel = []
    count = 0
    for i in range(len(s)):
        if s[i] not in spel:
            answer.append(-1)
            spel.append(s[i])
        else:
            spel.append(s[i])
            for j in range(len(spel)-1, -1, -1):
                if j == len(spel)-1:
                    continue
                if s[i] != spel[j]:
                    count += 1
                if s[i] == spel[j]:
                    count += 1
                    answer.append(count)
                    count = 0
                    break
    return answer