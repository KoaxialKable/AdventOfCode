file1 = open('Puzzle01_input.txt', 'r')
lines = file1.readlines()
  
# elf_number = 1
# elf_with_highest = 1
# highest_calorie = 0
# calorie = 0

# Part 1
# for line in lines:
#     if not line.strip() == '':
#         calorie += int(line)
#     else:
#         if calorie <= highest_calorie:
#             calorie = 0
#             elf_number += 1
#             pass
#         else:
#             elf_with_highest = elf_number
#             highest_calorie = calorie
#             calorie = 0
#             elf_number += 1


# Part 2
calorie = 0
elf1 = 0
elf2 = 0
elf3 = 0

for line in lines:
    if not line.strip() == '':
        calorie += int(line)
    else:
        if calorie > elf1:
            # new first
            elf3 = elf2
            elf2 = elf1
            elf1 = calorie
        elif calorie > elf2:
            # new second
            elf3 = elf2
            elf2 = calorie
        elif calorie > elf3:
            elf3 = calorie
        calorie = 0

print(f'Sum of three highest elves is {elf1+elf2+elf3}')