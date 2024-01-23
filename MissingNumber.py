n = input()
l = [int(i) for i in input().split()]
b.sort()
for k in range(int(n)+1):
    if k > 0:
        try:
            if k != b[k-1]:
                print(k)
                break
        except IndexError:
            print(k)
            break
    




