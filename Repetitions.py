import re
letter = input()
a,t,c,g = zip(*re.findall('(A*)(T*)(C*)(G*)', letter, re.DOTALL))
ans = [len(max(a)),len(max(t)), len(max(c)), len(max(g))]
print(a,t,c,g)
print(max(ans))
