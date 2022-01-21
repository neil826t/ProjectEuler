from copy import deepcopy as dcopy
def max_sum(t):
    msum = dcopy(t)
    for i in range(1, len(msum)):
        msum[i][0] += msum[i-1][0]
        #print(i, 0, "now", msum[i][0])
        msum[i][i] += msum[i-1][i-1]
        #print(i, i, "now", msum[i][0])
        for j in range(1, i):
            msum[i][j] += max(msum[i-1][j-1], msum[i-1][j])
            #print(i, j, "now", msum[i][j])
    return max(msum[-1])

with open('p067_triangle.txt') as f:
    lines = f.read().splitlines()
