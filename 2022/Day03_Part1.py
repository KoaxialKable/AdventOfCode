file1 = open('input files/Day03_input.txt', 'r')
lines = file1.readlines()

def number_value(char):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-38

total = 0
for line in lines:
    compartment_size = int(len(line.strip())/2)
    c1 = line.strip()[:compartment_size]
    c2 = line.strip()[compartment_size:]

    common = []
    for c in c1:
        if c in c2:
            if c not in common:
                common.append(c)
                total += number_value(c)
print(total)