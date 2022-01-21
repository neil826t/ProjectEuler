import numpy as np
def name_scores_fast(filename='p022_names.txt'):
    """Find the total of the name scores in the given file."""
    with open(filename, 'r') as infile:
        names = np.array(sorted(infile.read().replace('"', '').split(',')))
    # 2 list comprehensions with ord() to find letter value
    scores = [(num+1)*sum([ord(c)-64 for c in name]) for num, name in enumerate(names)]
    return sum(scores)