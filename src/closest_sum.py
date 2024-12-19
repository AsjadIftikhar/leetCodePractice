def closest_sum_to_target(numbers, targ):
    left, right = 0, len(numbers) - 1
    c_sum = 0
    c_pair = [left, right]
    while left < right:
        if numbers[left] + numbers[right] == targ:
            return targ, [left, right]
        if abs(numbers[left] + numbers[right] - targ) < abs(c_sum - targ):
            c_sum = numbers[left] + numbers[right]
            c_pair = [left, right]
        if numbers[left] + numbers[right] < targ:
            left += 1
        elif numbers[left] + numbers[right] > targ:
            right -= 1

    return c_sum, c_pair


# Sorted
nums = [1, 3, 5, 7, 10]
target = 15

print(closest_sum_to_target(nums, target))

# 10 < 15 -> left + 1, c_sum = 10
# 13 < 15 -> left + 1, c_sum = 13
# 14 < 15 -> left + 1, c_sum = 14
# 17 > 15 -> right - 1, out of loop
# c_sum = 14
