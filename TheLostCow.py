#https://usaco.org/index.php?page=viewproblem2&cpid=735
import sys

sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")

n = input()
j, c = (int(i) for i in n.split())
v = 1
s = j
count = 0
while True:
    t = s + v
    if (j <= c and c <= t) or (j >= c and c >= t):
        count += abs(c-j)
        break
    count += abs(t-j)
    v *= -2
    j = t
print(count)