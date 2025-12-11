def read_file(path):
    with open(path, "r") as john:
        cena = john.read()
    return cena


raw_data = read_file("2015/day6.csv").splitlines()

import matplotlib.pyplot as plt
import numpy as np

# Turn on = set to 1
# Toggle = set 0 to 1, set 1 to 0
# Turn off = set to 0

array = np.zeros((1000, 1000), dtype=int)


# print(raw_data)
def process_line(line):
    full = line.split(" ")
    command = full[0]
    if command == "turn":
        command = full[0] + full[1]
        range_start = full[2]
        range_end = full[4]
    elif command == "toggle":
        range_start = full[1]
        range_end = full[3]
    x1, y1 = range_start.split(",")
    x2, y2 = range_end.split(",")
    return command, int(x1), int(y1), int(x2), int(y2)


# for line in raw_data:
#     command, x1, y1, x2, y2 = process_line(line)
#     if command == "turnon":
#         array[y1 : y2 + 1, x1 : x2 + 1] = 1
#     elif command == "turnoff":
#         array[y1 : y2 + 1, x1 : x2 + 1] = 0
#     elif command == "toggle":
#         array[y1 : y2 + 1, x1 : x2 + 1] ^= 1
#     plt.clf()
#     plt.imshow(array, cmap="gray", interpolation="nearest")
#     plt.pause(0.001)  # small delay so it can draw

# # fig, ax = plt.subplots()
# # ax.imshow(array, cmap="gray", interpolation="nearest")
# # plt.show()

# print(sum(sum(array)))  # 543903


# ==================================== Part 2 ============================= #
#
array = np.zeros((1000, 1000), dtype=int)


# print(raw_data)
def process_line(line):
    full = line.split(" ")
    command = full[0]
    if command == "turn":
        command = full[0] + full[1]
        range_start = full[2]
        range_end = full[4]
    elif command == "toggle":
        range_start = full[1]
        range_end = full[3]
    x1, y1 = range_start.split(",")
    x2, y2 = range_end.split(",")
    return command, int(x1), int(y1), int(x2), int(y2)


for line in raw_data:
    command, x1, y1, x2, y2 = process_line(line)
    if command == "turnon":
        array[y1 : y2 + 1, x1 : x2 + 1] += 1
    elif command == "turnoff":
        array[y1 : y2 + 1, x1 : x2 + 1] = np.maximum(
            array[y1 : y2 + 1, x1 : x2 + 1] - 1, 0
        )
    elif command == "toggle":
        array[y1 : y2 + 1, x1 : x2 + 1] += 2
    # plt.clf()
    # plt.imshow(array, cmap="gray", interpolation="nearest")
    # plt.pause(0.001)  # small delay so it can draw

# fig, ax = plt.subplots()
# ax.imshow(array, cmap="gray", interpolation="nearest")
# plt.show()

print(sum(sum(array)))  # 14687245
