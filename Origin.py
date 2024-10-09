directions = input().strip()
d = {'U': 0, 'D': 0, 'R': 0, 'L': 0}
for direction in directions:
    if direction in d:
        d[direction] += 1
if d['U'] == d['D'] and d['R'] == d['L']:
    print("TRue")
else:
    print("False")
