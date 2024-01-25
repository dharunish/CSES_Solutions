t = input()
try:
    n = [int(i) for i in input().split()]
except IndexError:
    n = int(n)
index = 0
steps = 0
while True:
    if len(n) > 1:
        if n[index+1] < n[index]:
            steps = steps + n[index] - n[index+1]
            n[index+1] = n[index+1] + (n[index] - n[index+1])
        index += 1
        if index == int(t) - 1:
            break
    else:
        break
print(steps) 

