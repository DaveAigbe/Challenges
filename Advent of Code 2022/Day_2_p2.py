from Day_2_p1 import outcomes

"""
A = ROCK - 1pt
B = PAPER - 2pts
C = SCISSORS - 3pts

X = LOSE ROUND
Y = DRAW ROUND
Z = WIN ROUND   

LOSS = 0pts
DRAW = 3pts
WIN = 6pts
"""


score = 0

for r in outcomes:
    if r:
        opponent = r[0]
        if opponent == 'A':
            response = r[-1]

            match response:
                case 'X':
                    score += 3
                case 'Y':
                    score += 4
                case 'Z':
                    score += 8
        elif opponent == 'B':
            response = r[-1]

            match response:
                case 'X':
                    score += 1
                case 'Y':
                    score += 5
                case 'Z':
                    score += 9
        elif opponent == 'C':
            response = r[-1]

            match response:
                case 'X':
                    score += 2
                case 'Y':
                    score += 6
                case 'Z':
                    score += 7

print(score)
