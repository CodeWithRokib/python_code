nums = [1, 2, 3, 4, 5]
target = 6
pairs = [(x, y) for i, x in enumerate(nums) for y in nums[i+1:] if x + y == target]
print(pairs)
