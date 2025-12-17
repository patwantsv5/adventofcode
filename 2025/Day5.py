def read_file(path):
    with open(path, "r") as f:
        data = f.read()
    return data


test_data = read_file("2025/day5sample.csv")
raw_data = read_file("2025/day5.csv")


# =================================== Part 1 ===============================#
def split_strings(data):
    item_range, ingredients = data.split("\n\n")
    item_range = item_range.splitlines()
    ingredients = ingredients.splitlines()
    return item_range, ingredients


def check(i, ranges):
    for r in ranges:
        r1, r2 = r.split("-")
        each_range = range(int(r1), int(r2) + 1)
        # print(each_range)
        # print(i)
        if int(i) in each_range:
            # True
            return 1
    return 0


counts = 0
ranges, ingredients = split_strings(test_data)
for i in ingredients:
    counts += check(i, ranges)

print(f"part 1: {counts}")  # 613

# ============================================ Part 2 ============================================= #
# 3-5
# 10-14
# 12-18
# 16-20
data = []
count = 0
for r in ranges:
    r1, r2 = r.split("-")
    data.append([int(r1), int(r2)])
data = sorted(data)
print(data)
for idx, x in enumerate(data):
    length = len(data)
    # If last
    if idx + 1 == length:
        num = data[idx][1] - data[idx][0] + 1
        count += num
    # If overlaps
    elif x[1] >= data[idx + 1][0]:
        print(
            f"{x[1]} did overlap with {data[idx + 1][0]}, changed next idx+1 to [{x[0]}, {data[idx + 1][1]}]"
        )
        data[idx + 1][0] = x[0]
        if data[idx + 1][1] < data[idx][1]:
            data[idx + 1][1] = data[idx][1]
    # if not overlap
    elif x[1] < data[idx + 1][0]:
        num = data[idx][1] - data[idx][0] + 1
        print(f"{x[1]} did not overlap with {data[idx + 1][0]}, added {num} counts.")
        count += num

print(f"part 2 counts: {count}")  # 336495597913098 answer
