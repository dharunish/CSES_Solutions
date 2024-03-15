import sys
'''
sys.stdin = open("word.in", "r")
sys.stdout = open("word.out", "w")
'''

n = sys.stdin.readline()
n = [int(i) for i in n.split()]
s = sys.stdin.readline()
line = [i for i in s.split()]
newLine = ''
for i in range(n[0]):
    if newLine:
        check = newLine + line[i]
        check = check.replace(' ', '')
        if len(check) > n[1]:
            print(newLine)
            newLine = line[i]
        else:
            newLine += f' {line[i]}'
    else:
        newLine += line[i]

print(newLine)
