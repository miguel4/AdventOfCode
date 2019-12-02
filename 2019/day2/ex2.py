with open('input.txt') as f:
    original_nums = [int(line) for line in f.readlines()[0].split(',')]

for i in range(0, 100):
    for j in range(0, 100):
        nums = original_nums.copy()
        current = 0
        nums[1] = i
        nums[2] = j
        while nums[current] != 99:
            if nums[current] == 1:
                nums[nums[current + 3]] = nums[nums[current + 1]] + nums[nums[current + 2]]
            elif nums[current] == 2:
                nums[nums[current + 3]] = nums[nums[current + 1]] * nums[nums[current + 2]]
            current += 4

        if nums[0] == 19690720:
            print(nums)
            print(100 * nums[1] + nums[2])
