#http://www.usaco.org/index.php?page=viewproblem2&cpid=567
import sys

sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

a = sys.stdin.readline()
b = sys.stdin.readline()

c = a + ' ' + b
k = [int(i) for i in c.split()]
ans = max(k) - min(k)
if k[0] > k[3]:
    ans = (ans - (k[0] - k[3]))
elif k[2] > k[1]:
    ans = (ans-(k[2] - k[1]))
sys.stdout.write(str(ans))
