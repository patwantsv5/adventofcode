def read_file(path):
    with open(path, "r") as balls:
        data = balls.read()
    return data


test_data = read_file("2025/day7sample.csv")
raw_data = read_file("2025/day7.csv")


# =============================== Part 1 ===============================
#
def visualize(grid):
    for i in grid:
        string = ""
        for s in i:
            string = string + s
        print(string)


def count_beam_being_hit(grid):
    count = 0
    for row_num, row in enumerate(grid):
        for char_idx, char in enumerate(row):
            if char == "^" and grid[row_num - 1][char_idx] == "|":
                count += 1

    print(count)


# Turns the data into a grid
data = raw_data.splitlines()
grid = []

for i in data:
    boogie_woogie = []
    for d in i:
        boogie_woogie.append(d)
    grid.append(boogie_woogie)

length = len(grid)
# print(length)
# count = 0
changesMade = 0
while True:
    changesMade = 0
    for row_num, row in enumerate(grid):
        for char_idx, char in enumerate(row):
            # if S, change bottom to "|"
            if char == "S" and grid[row_num + 1][char_idx] == ".":
                grid[row_num + 1][char_idx] = "|"
                changesMade = 1
            # If "^", checks above if there is "|", if there is then shoots rays. if not do nothing.
            elif char == "^" and grid[row_num - 1][char_idx] == "|":
                if (
                    grid[row_num][char_idx - 1] == "."
                    or grid[row_num][char_idx + 1] == "."
                ):
                    grid[row_num][char_idx - 1] = "|"
                    grid[row_num][char_idx + 1] = "|"
                    # split count
                    # count += 1
                    changesMade = 1
            # for "|"
            # if "|"
            elif char == "|":
                if row_num + 1 < length and grid[row_num + 1][char_idx] == ".":
                    grid[row_num + 1][char_idx] = "|"
                    changesMade = 1
    if changesMade == 0:
        break

visualize(grid)
count_beam_being_hit(grid)  # 1598 Part 1 done
