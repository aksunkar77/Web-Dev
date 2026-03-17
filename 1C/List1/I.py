def sum2(nums):
    return sum(nums[:2])

nums = list(map(int, input().split()))
print(sum2(nums))