#https://usaco.org/index.php?page=viewproblem2&cpid=939

import sys

sys.stdin = open("buckets.in", "r")
sys.stdout = open("buckets.out", "w")

for i in range(10):
    n = sys.stdin.readline()
    if 'B' in n:
        yB = i + 1
        xB = n.index('B') + 1
    if 'L' in n:
        yL = i + 1
        xL = n.index('L') + 1

print((abs(yL-yB) + abs(xL - xB)) - 1)



