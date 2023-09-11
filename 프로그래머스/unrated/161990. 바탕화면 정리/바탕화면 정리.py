def solution(wallpaper):
    answer = []
    row_ = 0
    col_ = 0
    row_lst = []
    col_lst = []
    for i_index, i in enumerate(wallpaper):
        for j_index, j in enumerate(i):
            if j == '#':
                row_lst.append(i_index)
                col_lst.append(j_index)
    min_row = min(row_lst)
    min_col = min(col_lst)
    max_row = max(row_lst)+1
    max_col = max(col_lst)+1
    answer.extend([min_row, min_col, max_row, max_col])
    return answer