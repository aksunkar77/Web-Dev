def rotate_left3(nums):
    return nums[1:] + nums[:1]

nums = list(map(int, input().split()))
print(rotate_left3(nums))