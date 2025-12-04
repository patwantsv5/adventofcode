file_path = "2015/day1.csv"
# Import data
def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data

raw_data = read_data(file_path)


# ============ Part 1 ========== #
floor = 0
for x in raw_data:
    if x == '(':
        floor +=1
    elif x == ')':
        floor -=1

print(f"Part 1 Answer: {floor}")

# ============ Part 2 ===========#

floor = 0
for idx, y in enumerate(raw_data):
    if y == '(':
        floor +=1
    elif y == ')':
        floor -=1

    if floor == -1:
        position = idx + 1
        break

print(f"Part 2 Answer: {position}")