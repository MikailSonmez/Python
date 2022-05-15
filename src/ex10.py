largest = -1
print("before", largest)
for nums in [9, 6, 11, 45, 2, 99, 76, 8]:
    if nums > largest:
        largest = nums
    print(largest, nums)
print("after", largest)