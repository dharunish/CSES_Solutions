#https://codeforces.com/problemset/problem/546/A
import sys

a = sys.stdin.readline()
a = [int(i) for i in a.split()]
n = []
for i in range(a[-1]):
    n.append(a[0]*(i+1))
if sum(n) - a[1] <=0:
    sys.stdout.write('0')
else:
    sys.stdout.write(str(sum(n) - a[1]))