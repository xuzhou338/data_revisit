from sudoku_V02 import Sudoku


def determine_loc(loc):
    for i in range(9):
        if loc >= i * 9:
            n_row = i
    n_col = loc % 9

    block_head = [0, 3, 6, 27, 30, 33, 54, 57, 60]
    for i, head_num in enumerate(block_head):
        block_full = [head_num, head_num + 1, head_num + 2,
                      head_num + 9, head_num + 10,
                      head_num + 11, head_num + 18, head_num + 19,
                      head_num + 20]
        if loc in block_full:
            n_block = i
    return n_row, n_col, n_block


def record(loc, a, row_s, col_s, block_s):
    n_row, n_col, n_block = determine_loc(loc)
    row_s[n_row].append(a)
    col_s[n_col].append(a)
    block_s[n_block].append(a)
    return row_s, col_s, block_s

def display(s):
    for i in range(9):
        row_str = []
        for a_1 in s[9 * i:9 * i + 9]:
            row_str.append(str(a_1))
        print(' '.join(row_str[0:3]), '|', ' '.join(row_str[3:6]), '|',
              ' '.join(
                  row_str[6:9]))
        if i == 2 or i == 5:
            print('- - - - - - - - - - -')

def sorta(s):
    row, col, block = {}, {}, {}
    for i in range(9):
        row[i], col[i], block[i] = [], [], []
    empty_elem = []
    for loc in range(80):
        num = s[loc]
        if num == ' ':
            empty_elem.append(loc)
        else:
            n_row, n_col, n_block = determine_loc(loc)
            row[n_row].append(num)
            col[n_col].append(num)
            block[n_block].append(num)
    return empty_elem, row, col, block

def list_subtract(a, b):
    c = list(set(a) - set(b))
    return c

def available_choices(row, col, block):
    choice_full = list(range(1, 10))
    row_choices, col_choices, block_choices = {}, {}, {}
    for i in range(9):
        row_choices[i], col_choices[i], block_choices[i] = [], [], []
        row_choice = list_subtract(choice_full, row[i])
        col_choice = list_subtract(choice_full, col[i])
        block_choice = list_subtract(choice_full, block[i])

        row_choices[i] += row_choice
        col_choices[i] += col_choice
        block_choices[i] += block_choice
    return row_choices, col_choices, block_choices

def solve(s):
    empty_elem, row, col, block = sorta(s)
    retry = 1
    while True:
        if retry > 100:
            break
        row_choices, col_choices, block_choices = available_choices(row, col,
                                                                    block)
        for loc in empty_elem:
            n_row, n_col, n_block = determine_loc(loc)
            if len(row_choices[n_row]) == 1:
                s[loc] = row_choices[n_row]
                break
            elif len(col_choices[n_col]) == 1:
                s[loc] = col_choices[n_col]
                break
            elif len(block_choices[n_block]) == 1:
                s[loc] = block_choices[n_block]
                break
        empty_elem, row, col, block = sorta(s)
        retry += 1
        if empty_elem:
            continue

    return s

if __name__ == '__main__':
    for i in range(80):
        trial = Sudoku()
        p = trial.make_puzzle(i)
        s = trial.solution
        empty_elem, row, col, block = sorta(p)

        s1 = solve(p)
        print(i)
        if s == s1:
            print('Sucess!')
        else:
            print('Fail')


