def rotate(nums, m):
    m = m % len(nums)
    return nums[-m:] + nums[:-m]


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(rotate(nums, 13))
