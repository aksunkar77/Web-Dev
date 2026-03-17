def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

nums = list(map(int, input().split()))
print(first_last6(nums))