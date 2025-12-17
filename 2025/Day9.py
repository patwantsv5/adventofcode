def read_file(path):
    with open(path, "r") as gucci:
        data = gucci.read()
    return data


test_data = read_file("2025/day9sample.csv").splitlines()
raw_data = read_file("2025/day9.csv").splitlines()

print(test_data)


def find_area(coordinates_1, coordinates_2):
    # 2,5 and 9,7 would make 24
    area = 0
    x_1, y_1 = coordinates_1.split(",")
    x_2, y_2 = coordinates_2.split(",")
    x_1 = int(x_1)
    x_2 = int(x_2)
    y_1 = int(y_1)
    y_2 = int(y_2)
    # print(f"{x_1} {y_1} to {x_2} {y_2}")
    # X area
    if x_1 > x_2:
        x_area = x_1 - x_2 + 1
    elif x_2 > x_1:
        x_area = x_2 - x_1 + 1
    elif x_1 == x_2:
        x_area = 1
    # Y area
    if y_2 > y_1:
        y_area = y_2 - y_1 + 1
    elif y_1 > y_2:
        y_area = y_1 - y_2 + 1
    elif y_1 == y_2:
        y_area = 1

    area = x_area * y_area
    return area


area = []

data = raw_data
for idx, x in enumerate(data):
    length = len(data)
    for i in data[idx + 1 : length]:
        cookie = find_area(x, i)
        area.append(cookie)
        # print(cookie)

print(max(area))  # 5287451230 too high
