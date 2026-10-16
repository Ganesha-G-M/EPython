arr = list(map(int, input("Enter an array :"). split()))
target = int(input("Enetr taget value :"))
for i in range(len(arr)):
    if arr[i] == target:
        print("Value Found ", i)
        break
    else:
        print("Not found")