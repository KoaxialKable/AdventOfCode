file1 = open('input files/Day03_input.txt', 'r')
lines = file1.readlines()

def number_value(char):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-38

total = 0
l = 0
group = []

for line in lines:
    i = l%3
    compartment_size = int(len(line.strip())/2)
    c1 = line.strip()[:compartment_size]
    c2 = line.strip()[compartment_size:]

    group.append(line.strip())
    
    if i == 2:
        common = []
        for item in group[0]:
            if item in group[1] and item in group[2] and item not in common:
                common.append(item)
        for badge in common:
            total+=number_value(badge)
        group = []
    
    l+=1


print(total)