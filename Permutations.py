import random
t = int(input())
even = []
odd = []
if t > 3 or t == 1:
    for i in range(t+1):
        if i != 0:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
    for e in even:
        print(f'{e} ', end="")
    for o in odd:
        print(f'{o} ', end="")
else:
    print('NO SOLUTION')


