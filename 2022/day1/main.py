def solution():
    total = 0
    elves = []
    with open('./input') as food:
        for item in food:
            if item != '\n':
                total = total + int(item)
            else:
                elves.append(total)
                total = 0
    # Part 1 answer
    print(f"Part 1 answer: {max(elves)}")
    # Part 2 answer
    ans = sum(sorted(elves, reverse=True)[:3])
    print(f"Part 2 answer: {ans}")
    
solution()
