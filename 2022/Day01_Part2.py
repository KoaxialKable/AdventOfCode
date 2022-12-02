file1 = open('input files/Day01_input.txt', 'r')
lines = file1.readlines()
  
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