file1 = open('input files/Day04_input.txt', 'r')
lines = file1.readlines()

count = 0
for line in lines:
    pair = []
    chunks = line.strip().split(',')

    for chunk in chunks:
        vals = chunk.split('-')
        pair.append([int(vals[0]), int(vals[1])])

    if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]) or (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][0]):
        count+=1

print(count)