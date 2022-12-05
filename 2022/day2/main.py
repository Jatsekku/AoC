# Part1
def judge1(oponent, me):
    score = 0
    # {A;B;C} -> <0;2> 
    oponent = ord(oponent) - 65
    # {X;Y;Z} -> <0;2> 
    me = ord(me) - ord('X')

    if oponent == me:
        # Draw
        score = me + 3
    elif (me - oponent) % 3 == 1:
        # I won
        score = me + 6
    else:
        # I lose
        score = me

    return score+1

# Part2
def judge2(oponent, result):
    score = 0
    # {A;B;C} -> <0;2> 
    oponent = ord(oponent) - 65

    if result == 'Y':
        # Draw
        score = oponent + 3
    elif result == 'Z':
        # I won
        score = (oponent + 1) % 3 + 6
    elif result == 'X':
        # I lose
        score = (oponent - 1) % 3

    return score + 1

def solution():
    sum1 = 0
    sum2 = 0
    with open('./input') as strategy:
        for x in strategy:
            sum1 += judge1(x[0], x[2])
            sum2 += judge2(x[0], x[2])
        # Part 1 answer
        print(f"Part 1 answer: {sum1}")
        # Part 2 answer
        print(f"Part 2 answer: {sum2}")

solution()
