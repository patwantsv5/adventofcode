import os


def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()
    return data


test_data = """11-22,95-115,998-1012
,1188511880-1188511890,222220-222224,1698522-1698528,
446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

raw_data = """7777742220-7777814718,3201990-3447830,49-86,653243-683065,91-129,24-41,1-15,2678-4638,1407-2511,221-504,867867-942148,1167452509-1167622686,9957459726-9957683116,379068-535983,757-1242,955118-1088945,297342-362801,548256-566461,4926-10075,736811-799457,1093342-1130060,620410-651225,65610339-65732429,992946118-993033511,5848473-5907215,17190619-17315301,203488-286290,15631-36109,5858509282-5858695889,87824047-87984031,1313113913-1313147594,795745221-795825571,46303-100636,4743038-4844422
"""

input_test = []
input_raw = []

d = test_data.split(",")
for x in d:
    u = x.strip("\n")
    input_test.append(u)

d = raw_data.split(",")
for x in d:
    u = x.strip("\n")
    input_raw.append(u)
# print(f"Puzzle input: {input}")

## ============================== Part 1 ============================ ##

def part1(input):
    same_numbers = []
    for number in input:
        range1, range2 = number.split("-")
        for current_num in range(int(range1), int(range2)+1):
            current_num_str = str(current_num)
            # print(current_num_str)
        # CHECKS LENGTH OF INDIVIDUAL NUMBER
            length = len(str(current_num)) # 2 
            # print(current_num)
            # print(length)
            # Checks if len is even

            # print(length)
            if length % 2 == 0:
                middle_point = int(length / 2)
                first = current_num_str[0:middle_point]
                second = current_num_str[middle_point:length]
                # print(first)
                # print(second)
                if first == second:
                    same_numbers.append(int(first + second))
    return same_numbers


invalid_ids = part1(input_raw)
answer = sum(invalid_ids)
print(answer)


## ============================ Part 2 ============================= ##

