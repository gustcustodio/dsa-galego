nums = [1, 3, 4, 6, 8, 10, 13]
target = 13


def twoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return False

print(twoSum(nums, target))