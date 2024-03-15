#https://usaco.org/index.php?page=viewproblem2&cpid=761
import sys
'''
sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")
'''
n = int(input())
l = []
for i in range(n):
    s = input().split()
    s[0] = int(s[0])
    s[2] = int(s[2])
    l.append(s)
l.sort()
b = 7
m = 7
e = 7
count = 0
for i in l:
    rank = [b,m,e]
    v = rank[2]
    rank.sort()
    if v != rank[2]:
        count += 1
    if i[1] == 'Bessie':
        b = b + i[2]
    elif i[1] == 'Elsie':
        e = e + i[2]
    elif i[1] == 'Mildred':
        m = m + i[2]

print(count)