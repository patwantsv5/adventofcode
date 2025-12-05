file_pathx = "2025/day4.csv"

def load_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data

raw_data = load_file(file_pathx)
test_data = load_file("2025/day4sample.csv")
# ================== Part 1 ================== #
data = raw_data.splitlines()

def pad_data(data):
    added_row = []
    length_x = len(data[0]) + 2
    rows = ["." * length_x]
    new = rows + data
    for x in data:
        added_row.append("." + x + ".")
    added_row = rows + added_row + rows
    # print(added_row)
    return added_row

paper_rolls_removed = 0
new_data = pad_data(data)
# print(new_data)
answer_data = new_data.copy()
answer_grid = [list(row) for row in answer_data]
# print(data)
for ix, x in enumerate(new_data): # PICKS ROWS @@@@@@@@@@..
    copy_data = new_data.copy()
    for idx, d in enumerate(x): # PICKS SPECIFIC CHARACTER '@'
        neighbor_max = 4
        if d == '@':
            # If first row.
            # Top Right
            if new_data[ix-1][idx -1] == '@':
                neighbor_max -= 1
            # Top Left
            if new_data[ix-1][idx +1] == '@':
                neighbor_max -= 1
            # Top
            if new_data[ix-1][idx] == '@':
                neighbor_max -= 1
            # Left
            if new_data[ix][idx+1] == '@':
                neighbor_max -= 1
            # Right
            if new_data[ix][idx-1] == '@':
                neighbor_max -= 1
            # Down
            if new_data[ix+1][idx] == '@':
                neighbor_max -= 1
            # Bottom Left
            if new_data[ix+1][idx+1] == '@':
                neighbor_max -= 1
            # Bottom Right
            if new_data[ix+1][idx-1] == '@':
                neighbor_max -= 1
            # If less than 4

            if neighbor_max > 0:
                answer_grid[ix][idx] = 'x'
                paper_rolls_removed += 1
        else:
            answer_grid[ix][idx] = '.'

# print(answer_grid)
paper_rolls = 0
for x in answer_grid:
    paper_rolls += x.count('x')
# print(paper_rolls_removed)
print(f"Answer part 1 : {paper_rolls}")

# ============================================ Part 2 ===================================== #
def pad_data(data):
    added_row = []
    length_x = len(data[0]) + 2
    rows = ["." * length_x]
    new = rows + data
    for x in data:
        added_row.append("." + x + ".")
    added_row = rows + added_row + rows
    # print(added_row)
    return added_row

def part2(new_data, answer_grid):
    continues = True
    while continues:
        replaced_number = 0
        for ix, x in enumerate(new_data): # PICKS ROWS @@@@@@@@@@..
            for idx, d in enumerate(x): # PICKS SPECIFIC CHARACTER '@'
                neighbor_max = 4
                if d == '@':
                    # If first row.
                    # Top Right
                    if new_data[ix-1][idx -1] == '@':
                        neighbor_max -= 1
                    # Top Left
                    if new_data[ix-1][idx +1] == '@':
                        neighbor_max -= 1
                    # Top
                    if new_data[ix-1][idx] == '@':
                        neighbor_max -= 1
                    # Left
                    if new_data[ix][idx+1] == '@':
                        neighbor_max -= 1
                    # Right
                    if new_data[ix][idx-1] == '@':
                        neighbor_max -= 1
                    # Down
                    if new_data[ix+1][idx] == '@':
                        neighbor_max -= 1
                    # Bottom Left
                    if new_data[ix+1][idx+1] == '@':
                        neighbor_max -= 1
                    # Bottom Right
                    if new_data[ix+1][idx-1] == '@':
                        neighbor_max -= 1
                    # If less than 4

                    if neighbor_max > 0:
                        answer_grid[ix][idx] = 'x'
                        replaced_number += 1
                elif d == 'x':
                    answer_grid[ix][idx] = 'x'
                else:
                    answer_grid[ix][idx] = '.'
        print(replaced_number)
        new_data = answer_grid
        if replaced_number == 0:
            break
    return answer_grid
        
data = raw_data.splitlines()

paper_rolls = 0
new_data = pad_data(data)
# print(new_data)
answer_data = new_data.copy()
answer_grid = [list(row) for row in answer_data]
# print(data)

answer_grid = part2(new_data, answer_grid)
print(answer_grid)
# print(answer_grid)
for x in answer_grid:
    paper_rolls += x.count('x')
# print(paper_rolls_removed)
print(f"Answer part 2 : {paper_rolls}") # 9784
