file_pathx = "2025/day4.csv"

def load_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data

raw_data = load_file(file_pathx)
test_data = load_file("2025/day4sample.csv")
# ================== Part 1 ================== #
data = test_data.splitlines()

def pad_data(data):
    added_row = []
    length_x = len(data[0]) + 2
    rows = ["." * length_x]
    new = rows + data
    for x in data:
        added_row.append("." + x + ".")
    added_row = rows + added_row + rows
    print(added_row)
    return added_row

new_data = pad_data(data)

answer_data = new_data.copy()
print(data)
for ix, x in enumerate(new_data): # PICKS ROWS @@@@@@@@@@..
    copy_data = new_data.copy()
    neighbor_max = 4
    for idx, d in enumerate(x): # PICKS SPECIFIC CHARACTER '@'
        if d == '@':
            # If first row.
            if ix == 0:
                # Top Right
                if data[ix-1][idx -1] == '@':
                    neighbor_max -= 1
                # Top Left
                if data[ix-1][idx +1] == '@':
                    neighbor_max -= 1
                # Top
                if data[ix-1][idx] == '@':
                    neighbor_max -= 1
                # Left
                if data[ix][idx+1] == '@':
                    neighbor_max -= 1
                # Right
                if data[ix][idx-1] == '@':
                    neighbor_max -= 1
                # Down
                if data[ix+1][idx] == '@':
                    neighbor_max -= 1
                # Bottom Left
                if data[ix+1][idx+1] == '@':
                    neighbor_max -= 1
                # Bottom Right
                if data[ix+1][idx-1] == '@':
                    neighbor_max -= 1
                # If less than 4
                if neighbor_max > 0:
                    answer_data[ix][idx] == 'x'

print(answer_data)