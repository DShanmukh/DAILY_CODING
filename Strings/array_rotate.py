n = list(map(int,input().split()))
k = list(map(int,input().split()))
k1 = n[0]
left = 0
right = len(n) - 1
while left  <= right:
  mid = (left+right) // 2
  if k[mid] == max(k):
    print(mid+1)
  elif k[mid - 1] > k[mid] > k[mid + 1] or k[mid - 1] < k[mid] > k[mid + 1]:
    if k[mid - 1] > k[mid + 1]:
      left = mid + 1
      right = len(k) - 1
    else:
      right = mid - 1
      left = 0
  elif k[mid - 1] < k[mid] < k[mid- 1]:
    right = mid - 1
    left = mid + 1
  
  
  