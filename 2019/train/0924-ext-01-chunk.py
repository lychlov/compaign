def chunk(nums, n):
    length = len(nums)
    if n >= length:
        return [nums]
    temp = [nums[i:i + n] for i in range(0, length, n)]
    return temp


print(chunk([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 7))
