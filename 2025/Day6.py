def read_file(path):
    with open(path, "r") as f:
        data = f.read()
    return data


raw_data = read_file("2025/day6.csv")
test_data = read_file("2025/day6sample.csv")

# print(test_data)
data = []
data = test_data.splitlines()

numbers = []
operations = []
for idx, x in enumerate(data):
    single = x.split(" ")
    single = list(filter(lambda d: d.strip(), single))
    if idx + 1 == len(data):
        operations.append(single)
    else:
        numbers.append(single)

# ====================================== Part 1 ======================================== #
#


def calculate_column(numbers, operations):
    total_columns = []
    length = len(numbers)
    for idx, i in enumerate(operations):
        ea_op = []
        # print(f"idx:{idx}, i:{i}")
        # Store equal to the amount of rows.
        for k in range(0, length):
            ea_op.append(numbers[k][idx])
            # print(ea_op)
        if i == "*":
            value_to_add = 0
            for num in ea_op:
                if value_to_add == 0:
                    value_to_add += int(num)
                else:
                    value_to_add = value_to_add * int(num)
        elif i == "+":
            value_to_add = 0
            for num in ea_op:
                value_to_add += int(num)
        total_columns.append(value_to_add)

        # print(total_columns)
    return sum(total_columns)


# operations = operations[0]

# print(f"Numbers : {numbers}")
# print(f"Operations : {operations}")
# print(f"Part 1 : {calculate_column(numbers, operations)}")  # part 1 : 3968933219902

# ========================== Part 2 ============================================#
#

test_data = read_file("2025/day6sample.csv").splitlines()
raw_data = read_file("2025/day6.csv").splitlines()
new_data = []
operations = []

grid = []
for line in test_data:
    sentence = []
    for x in line:
        sentence.append(x)
    grid.append(sentence)

print(grid)
