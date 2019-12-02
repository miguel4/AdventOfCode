with open('input.txt') as f:
    nums = [int(line) for line in f.readlines()[0].split(',')]

current = 0
nums[1] = 12
nums[2] = 2
while nums[current] != 99:
    if nums[current] == 1:
        nums[nums[current + 3]] = nums[nums[current + 1]] + nums[nums[current + 2]]
    elif nums[current] == 2:
        nums[nums[current + 3]] = nums[nums[current + 1]] * nums[nums[current + 2]]
    current += 4

print(nums)
