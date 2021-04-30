from copy import deepcopy

def combination_sum_helper(nums, start, result, remainder, combination, length):

    if remainder == 0:
        if length == len(combination):
            result.append(deepcopy(combination))
        return
    elif remainder < 0:
        return 
    for i in range(start, len(nums)):
        combination.append(nums[i])
        combination_sum_helper(nums, i+1, result, remainder-nums[i], combination, length)
        combination.pop()


def combination_sum(length, target):
    result = []
    key = [1,2,3,4,5,6,7,8,9]
    combination_sum_helper(key,0, result, target, [], length)
    print(result)

print(combination_sum(3,9))
