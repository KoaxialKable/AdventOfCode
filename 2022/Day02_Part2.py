file1 = open('input files/Day02_input.txt', 'r')
lines = file1.readlines()

# Rock:    A
# Paper:   B
# Scissor: C

# X, lose
# Y, draw
# Z, win

result = {
    'A X': 3, 'A Y': 4, 'A Z': 8,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7,
}
score = 0

for line in lines:
    score += result[line.strip()]

print(score)