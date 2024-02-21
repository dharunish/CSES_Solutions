#https://codeforces.com/problemset/problem/231/A
import sys
'''
sys.stdin = open("teleport.in", "r")
sys.stdout = open("teleport.out", "w")
'''

n = int(sys.stdin.readline())
c = 0
for i in range(n):
    a = sys.stdin.readline()
    a = [int(p) for p in a.split()]
    if sum(a) >= 2:
        c += 1
sys.stdout.write(str(c))