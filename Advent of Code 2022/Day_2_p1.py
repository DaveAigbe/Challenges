from Day_2_Data import outcomes

"""
A, X = ROCK - 1pt
B, Y = PAPER - 2pts
C, Z = SCISSORS - 3pts

LOSS = 0pts
DRAW = 3pts
WIN = 6pts
"""

outcomes = outcomes.split('\n')

score = 0

for r in outcomes:
    if r:
        opponent = r[0]
        if opponent == 'A':
            response = r[-1]

            match response:
                case 'X':
                    score += 4
                case 'Y':
                    score += 8
                case 'Z':
                    score += 3
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
                    score += 7
                case 'Y':
                    score += 2
                case 'Z':
                    score += 6

# print(score)
