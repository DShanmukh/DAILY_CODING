s = input()
h = input()
p = []
for i in range(len(s)):
  if len(p) == len(h):
    print(p)
  else:
    p.append(s[i])