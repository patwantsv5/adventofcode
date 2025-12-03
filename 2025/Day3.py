def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()
    return data

test_data = read_data("2025/day3sample.csv")
raw_data = read_data("2025/day3.csv")

print(test_data)

# ========================= Part 1 ===========================#

def get_jolt(batteries):
    length = len(batteries)
    first_num = 0
    second_num = 0
    position = 0
    # First character
    for x in range(0, length -1):
        if int(batteries[x]) > first_num:
            first_num = int(batteries[x])
            position = x

    print(position)

    # Second character
    for x in range(position + 1, length):
        if int(batteries[x]) > second_num:
            second_num = int(batteries[x])

    print(int(str(first_num)+str(second_num)))

    return int(str(first_num)+str(second_num))

total_jolt = 0
for x in raw_data:
    total_jolt += get_jolt(x)

print(f"Total jolt: {total_jolt}")

# ======================== Part 2 ==============================#