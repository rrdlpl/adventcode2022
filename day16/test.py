from itertools import count, product, permutations, pairwise, combinations, combinations_with_replacement  # NOQA


comb = combinations(set(['DD', 'II', 'BB']), 2)

for c in comb:
    print(c)
