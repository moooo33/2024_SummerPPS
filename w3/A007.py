nums = [int(i) for i in input().split()]
nums_o = sorted(nums)
# print(nums, nums_o)

# 0: asc, 1: desc, 2: mixed
if nums == nums_o : print('ascending')
elif nums == nums_o[::-1] : print('descending')
else : print('mixed')