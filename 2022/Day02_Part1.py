file1 = open('input files/Day02_input.txt', 'r')
lines = file1.readlines()

# Rock:    A, X
# Paper:   B, Y
# Scissor: C, Z
win  = ['A Y', 'B Z', 'C X']
lose = ['A Z', 'B X', 'C Y']
draw = ['A X', 'B Y', 'C Z']

shapes = {'X': 1, 'Y': 2, 'Z': 3}
score = 0

for line in lines:
    if line.strip() in win:
        score += 6
    elif line.strip() in lose:
        score += 0
    elif line.strip() in draw:
        score += 3
    score += shapes[line.strip()[-1]]

print(score)