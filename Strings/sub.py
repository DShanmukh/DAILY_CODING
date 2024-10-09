# n = input("Enter a string: ")

# Function to check if all characters in a substring are unique
# def all_unique(substring):
#     return len(set(substring)) == len(substring)
# l =[]
# Iterate over all possible substrings
# for i in range(len(n)):
#     for j in range(i + 1, len(n) + 1):
#         k = n[i:j]
#         if all_unique(k):
#             l.append(len(k))
# print(max(l))
candidates = list(map(int,input().split()))
target = int(input())
n = []
k = 0
for i in range(len(candidates)):
    for j in range(len(candidates)):
        if candidates[i] + candidates[j] < target:
            k = target - (candidates[i] + candidates[j])
            if k in candidates:
                n.append(candidates[i])
                n.append(candidates[j])
                n.append(k)
    if candidates[i],candidates[j],candidates[k]  in n:
        n.remove(candidates[i],candidates[j],candidates[k])
print(n)