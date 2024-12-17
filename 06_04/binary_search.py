import random


def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while high >= low:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif target > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


n = 10
max_val = 100
data = [random.randint(1, max_val) for i in range(n)]
data.sort()
print("Data:", data)
target = int(input("Enter target value: "))
target_pos = binary_search(data, target)
if target_pos == -1:
    print("Your target value is not in the list.")
else:
    print("You target value has been found at index", target_pos)
