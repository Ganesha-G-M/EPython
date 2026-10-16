arr = [10,20,30,40,50,60]
target = 30
low = 0
high = len(arr) -1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print("index in ", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid -1
else:
    print("Not found")