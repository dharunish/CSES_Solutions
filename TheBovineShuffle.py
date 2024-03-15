import sys

sys.stdin = open("shuffle.in", "r")
sys.stdout = open("shuffle.out", "w")

n = input()
shuffle = [int(i) for i in input().split()]
id = [int(i) for i in input().split()]
for i in range(3):
    order = []
    for i in range(len(shuffle)):
        p = shuffle.index(i+1)
        order.append(id[p])
for i in order:
    print(i)