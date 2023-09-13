def solution(players, callings):
    pl_idx = {}
    for i_index, i in enumerate(players):
        pl_idx[i] = i_index
    
    for i in callings:
        a = pl_idx[i]
        pl_idx[i] -= 1
        pl_idx[players[a-1]] += 1
        players[a], players[a-1] = players[a-1], players[a]
    return players