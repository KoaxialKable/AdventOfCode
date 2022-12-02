file1 = open('input files/Day01_input.txt', 'r')
lines = file1.readlines()
  
elf_number = 1
elf_with_highest = 1
highest_calorie = 0
calorie = 0

# Part 1
for line in lines:
    if not line.strip() == '':
        calorie += int(line)
    else:
        if calorie <= highest_calorie:
            calorie = 0
            elf_number += 1
            pass
        else:
            elf_with_highest = elf_number
            highest_calorie = calorie
            calorie = 0
            elf_number += 1
        
print(highest_calorie)