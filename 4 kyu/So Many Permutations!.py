from itertools import permutations as permut

def permutations(s):
    return list(set(''.join(p) for p in permut(s, len(s))))