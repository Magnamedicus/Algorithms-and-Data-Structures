

#find the greatest continuous sub-array in an array of integers

def max_subarray(nums):

    if not nums:
        return 0

    current_max = nums[0]
    global_max = nums[0]

    for num in nums[1:]:

        current_max = max(num, current_max + num)
        global_max = max(global_max, current_max)

    return global_max


nums = [4,3,12,-9,4,-6,11,2,7,-10,1]

print(max_subarray(nums))