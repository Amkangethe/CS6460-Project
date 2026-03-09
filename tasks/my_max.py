def my_max(nums: list[int]) -> int:

    maximum = 0

    for num in nums:
        if num > maximum:
            maximum = num

    return maximum