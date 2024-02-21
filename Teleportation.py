import sys

sys.stdin = open("teleport.in", "r")
sys.stdout = open("teleport.out", "w")


n = sys.stdin.readline()
n = [int(i) for i in n.split()]
loc = []
tel = []
for i in range(2):
    loc.append(n[i])
for i in range(2):
    tel.append(n[i+2])

a = (abs(min(loc)-min(tel))) + (abs(max(loc) - max(tel)))
if a > (max(loc)-min(loc)):
    sys.stdout.write(str(max(loc)-min(loc)))
else:
    sys.stdout.write(str(a))




