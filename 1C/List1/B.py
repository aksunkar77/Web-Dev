def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

nums = list(map(int, input().split()))
print(same_first_last(nums))