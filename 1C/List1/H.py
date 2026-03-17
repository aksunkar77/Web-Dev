def max_end3(nums):
    m = max(nums[0], nums[-1])
    return [m] * 3

nums = list(map(int, input().split()))
print(max_end3(nums))