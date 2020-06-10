from itertools import combinations
def solution(num_buns, num_required):
    # Your code here
    rings = [[] for num in range(num_buns)]
    copies_per_key = num_buns - num_required + 1
    for key, bunnies in enumerate(combinations(range(num_buns), copies_per_key)):
        for bunny in bunnies:
            rings[bunny].append(key)

    return rings
