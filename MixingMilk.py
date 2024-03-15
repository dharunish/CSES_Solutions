import sys

sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")

b1 = sys.stdin.readline()
b1 = [int(i) for i in b1.split()]
b2 = sys.stdin.readline()
b2 = [int(i) for i in b2.split()]
b3 = sys.stdin.readline()
b3 = [int(i) for i in b3.split()]
for i in range(33):
    m = min(b2[0]-b2[1], b1[1])
    b2[1] += m
    b1[1] -= m
    m = min(b3[0]-b3[1], b2[1])
    b3[1] += m
    b2[1] -= m
    m = min(b1[0]-b1[1], b3[1])
    b1[1] += m
    b3[1] -= m

m = min(b2[0]-b2[1], b1[1])
b2[1] += m
b1[1] -= m
print(b1[1])
print(b2[1])
print(b3[1])