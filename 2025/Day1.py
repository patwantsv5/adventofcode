import os
import csv

file_path = "2025/day1.csv"
# Import data
def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()
    return data

# Print an array row by row
def print_array_rows(arr):
    for row in arr:
        print(row)

data = read_data(file_path=file_path)

# L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82

## ======================= Part 1 ================================##

# current_lock = 50   # Starting dial
# password = 0        # Pass
# for command in data:    
#     print(command)
#     sequence = command.strip("LR")      # Sequence = fucking number 19238129371283719283
#     if command.startswith('L'):         # Command = Left or right +-------==-=-=+-
#         current_lock = current_lock - int(sequence)
#         current_lock = current_lock % -100
#     elif command.startswith('R'):
#         current_lock = current_lock + int(sequence)
#         current_lock = current_lock % 100
#     print(current_lock)
#     if current_lock == 0:
#         password+=1
# print(password)


## ======================== Part 2 ============================== ## 
#R631
# 6892
# 6805-6911 too high

current_lock = 50   # Starting dial
password = 0        # Pass
for command in data:    
    print(command)
    sequence = int(command.strip("LR"))      # Sequence = fucking number 19238129371283719283
    if command.startswith('L'):         # Command = Left or right +-------==-=-=+-
        for i in range(sequence):
            current_lock-=1
            if current_lock == 0:
                password+=1
            if current_lock == -1:
                current_lock = 99

            print(current_lock)

    elif command.startswith('R'):
        for i in range(sequence):
            current_lock+=1
            if current_lock == 100:
                password+=1
                current_lock -= 100
            print(current_lock)

print(f"Password: {password}")

