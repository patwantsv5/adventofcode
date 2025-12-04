def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()
    return data

test_data = read_data("2025/day3sample.csv")
raw_data = read_data("2025/day3.csv")

print(test_data)

# ========================= Part 1 ===========================#

# def get_jolt(batteries):
#     length = len(batteries)
#     first_num = 0
#     second_num = 0
#     position = 0
#     # First character
#     for x in range(0, length -1):
#         if int(batteries[x]) > first_num:
#             first_num = int(batteries[x])
#             position = x

#     print(position)

#     # Second character
#     for x in range(position + 1, length):
#         if int(batteries[x]) > second_num:
#             second_num = int(batteries[x])

#     print(int(str(first_num)+str(second_num)))

#     return int(str(first_num)+str(second_num))

# total_jolt = 0
# for x in raw_data:
#     total_jolt += get_jolt(x)

# print(f"Total jolt: {total_jolt}")

# ======================== Part 2 ==============================#

# Loop from start up to max length - 12 for first number, then reduce to 11, for next number, over and over?
#

def get_val(batteries, position, digits, length):
    best_val = -1
    best_index = position
    for x in range(position, length - digits + 1):
        current = int(batteries[x])
        print(f"exce: {x}, battery[x]: {int(batteries[x])} compared to: {best_val}")
        if current > best_val:
            best_val = current
            best_index = x
            print(f"Set value to {best_val}, at index: {best_index}")
        
    return best_val, best_index + 1

def get_jolt_part2(batteries):
    print(batteries)
    length = len(batteries)
    twelve_char = [0] * 12
    position = 0
    digits = 12
    for seq, value in enumerate(twelve_char):
        # print(seq, value)
        number, position = get_val(batteries, position, digits, length)
        digits-=1
        # GET THE SINGULAR HIGHEST VALUE FIRSTTTTTTTTTTTTTTT
        print(position, number)
        twelve_char[seq] = number
    print(twelve_char)

    # # Second character
    # for x in range(position + 1, length):

    # print(int(str(first_num)+str(second_num)))
    total = ""
    for i in twelve_char:
        total = total+ str(i)
    return int(total)

total_jolt = 0
for x in raw_data:
    total_jolt += get_jolt_part2(x)

# total_jolt = get_jolt_part2("818181911112111")

print(f"Total jolt: {total_jolt}")