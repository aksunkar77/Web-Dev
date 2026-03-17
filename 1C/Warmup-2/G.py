def array_count9(nums):
    count = 0
    for n in nums:
        if n == 9:
            count += 1
    return count

print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9]))
print(array_count9([1, 9, 9, 3, 9]))