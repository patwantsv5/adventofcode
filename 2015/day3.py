path = "2015/day3.csv"

def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data

raw_data = read_data(path)
test_data = "^>v<"
test_data2 = "^v^v^v^v^v"
# ================ Part 1 =================== #

visited_house = []
        # x, y
path = [0,0]
visited_house.append(path.copy()) # count the first path.
for x in raw_data:
    # north
    if x == '^':
        path[1] += 1
        visited_house.append(path.copy())
    elif x == '>':
        path[0] += 1
        visited_house.append(path.copy())
    elif x == 'v':
        path[1] -= 1
        visited_house.append(path.copy())
    elif x == '<':
        path[0] -= 1
        visited_house.append(path.copy())
# 2080 too low
unique_house = []
for u in visited_house:
    if u not in unique_house:
        unique_house.append(u)
print(f"part 1 : {len(unique_house)}")

# ======================= Part 2 =================== #

visited_house = []
        # x, y
santa_path = [0,0]
robo_santa_path = [0,0]
visited_house.append(santa_path.copy()) # count the first path.
for idx,x in enumerate(raw_data):
    # north
    if x == '^':
        if idx % 2 == 0 or idx == 0: # santa
            santa_path[1] += 1
            visited_house.append(santa_path.copy())
        if idx % 2 != 0: # robosanta
            robo_santa_path[1] += 1
            visited_house.append(robo_santa_path.copy())
    elif x == '>':
        if idx % 2 == 0 or idx == 0: # santa
            santa_path[0] += 1
            visited_house.append(santa_path.copy())
        if idx % 2 != 0: # robosanta
            robo_santa_path[0] += 1
            visited_house.append(robo_santa_path.copy())
    elif x == 'v':
        if idx % 2 == 0 or idx == 0: # santa
            santa_path[1] -= 1
            visited_house.append(santa_path.copy())
        if idx % 2 != 0: # robosanta
            robo_santa_path[1] -= 1
            visited_house.append(robo_santa_path.copy())
    elif x == '<':
        if idx % 2 == 0 or idx == 0: # santa
            santa_path[0] -= 1
            visited_house.append(santa_path.copy())
        if idx % 2 != 0: # robosanta
            robo_santa_path[0] -= 1
            visited_house.append(robo_santa_path.copy())
# 2342 too high
unique_house = []
for u in visited_house:
    if u not in unique_house:
        unique_house.append(u)
print(f"part 2 : {len(unique_house)}")