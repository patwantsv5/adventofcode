def read_file(path):
    with open(path, 'r') as f:
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
    vows = ['a', 'e', 'i', 'o', 'u']
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
        if string[idx+1] == char:
            # contains two in a row
            return True
    return False

def check_bad_letters(string):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    length = len(string)
    for idx, char in enumerate(string):
        if idx + 1 == length:
            return True
        if char + string[idx+1] in forbidden:
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
print(part1) # 238 answer
