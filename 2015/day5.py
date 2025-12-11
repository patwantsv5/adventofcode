def read_file(path):
    with open(path, "r") as f:
        data = f.read()
    return data


raw_data = read_file("2015/day5.csv").splitlines()
test_data = read_file("2015/day5example.csv").splitlines()
# A nice string is one with all of the following properties:
#
#    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# ====================================== Part 1 ======================================= #


def check_vowels(string):
    vows_count = 0
    vows = ["a", "e", "i", "o", "u"]
    for char in string:
        if char in vows:
            vows_count += 1
    if vows_count >= 3:
        # Pass
        return True
    else:
        return False


def check_twice_letters(string):
    length = len(string)
    for idx, char in enumerate(string):
        if idx + 1 == length:
            return False
        if string[idx + 1] == char:
            # contains two in a row
            return True
    return False


def check_bad_letters(string):
    forbidden = ["ab", "cd", "pq", "xy"]
    length = len(string)
    for idx, char in enumerate(string):
        if idx + 1 == length:
            return True
        if char + string[idx + 1] in forbidden:
            # contains two in a row
            return False
    return True


part1 = 0
for i in raw_data:
    if check_vowels(i) == True:
        # print(f"{i} pass the check for check vows")
        if check_twice_letters(i) == True:
            # print(f"{i} pass the check for twice letters")
            if check_bad_letters(i) == True:
                # print(f"{i} pass the check for forbidden letters")
                part1 += 1
print(f"Part 1 Answer : {part1}")  # 238 answer


# =================================================== Part 2 ======================================================== #
# Conditions 1
# It contains a pair of any two letters that appears at least twice in the string without overlapping,
# like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# Conditions 2
# It contains at least one letter which repeats with exactly one letter between them,
# like xyx, abcdefeghi (efe), or even aaa.


# Only checks the pair of two characters
def create_pairs(string):
    length = len(string)
    for idx, x in enumerate(string):
        if idx + 1 == length:
            break
        pair = x + string[idx + 1]
        memo.append(pair)
    return memo


def check_pairs(memo):
    # print(memo)
    length = len(memo)
    for idx, x in enumerate(memo):
        # if idx == length:
        #     return False
        sub = memo[idx + 2 : length]
        if x in sub:
            match_index = sub.index(x) + idx + 2
            print(f"Found repeating pairs {x}@{idx} at {match_index}")
            return True
    return False


def check_space(string):
    length = len(string)
    for idx, char in enumerate(string):
        # None / At last idx, return False
        if idx + 2 == length:
            return False
        # if next-two idx is same then check middle
        if char == string[idx + 2]:
            # if char != string[idx + 1]:
            #     print(
            #         f"Found repeating char {char}@{idx} and {string[idx + 2]}@{idx + 2}"
            #     )
            return True
    return False


part2 = 0
for i in raw_data:
    memo = []
    memo = create_pairs(i)
    if check_pairs(memo) == True:
        print(f"{i} pass the check for check vows")
        if check_space(i) == True:
            print(f"{i} pass the check for twice letters")
            part2 += 1
    # print(memo)
print(part2)  # 69
