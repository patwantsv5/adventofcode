file = "2015/day2.csv"
def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()
    return data
raw_data = read_data(file)
# ============= Part 1 ============ #
# surface area of the box, which is 2*l*w + 2*w*h + 2*h*l
# (length l, width w, and height h)

def get_lwh(input):
    l, w, h = input.split('x')
    a = int(l) * int(w)
    b = int(w) * int(h)
    c = int(h) * int(l)
    surface = 2 * a + 2 * b + 2 * c
    extra = min([a,b,c])

    # print(surface, extra)
    return surface + extra

part1 = 0
for x in raw_data:
    part1 += get_lwh(x)
# part1 = get_lwh("2x3x4")

# 1464826 too low
print(f"Part 1 Answer: {part1}")

# ============= Part 2 ============= #

def get_lwh_part2(input):
    l, w, h = input.split('x')
    a = 2* (int(l) + int(w))
    b = 2* (int(w) + int(h))
    c = 2* (int(h) + int(l))
    bow = int(l) * int(w) * int(h)
    extra = min([a,b,c])

    print(bow, extra)
    return bow + extra

# 3944695 too high
part2 = 0
for x in raw_data:
    part2 += get_lwh_part2(x)
# part2 = get_lwh_part2("2x3x4")

# 1464826 too low
print(f"Part 2 Answer: {part2}")