file1 = open('input files/Day04_input.txt', 'r')
lines = file1.readlines()

count = 0
for line in lines:
    pair = []
    size = []
    chunks = line.strip().split(',')

    for chunk in chunks:
        vals = chunk.split('-')
        pair.append([int(vals[0]), int(vals[1])])
    
    for set in pair:
        size.append(set[1] - set[0])

    if size[0] > size[1]:
        s = pair[1]
        b = pair[0]
    else:
        # in cases where the size is the same, ordering doesn't matter
        s = pair[0]
        b = pair[1]
    
    if s[0] >= b[0] and s[1] <= b[1]:
        count += 1
print(count)