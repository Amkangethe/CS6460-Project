def running_sum(nums: list[int]) -> list[int]:

    result = []

    for i in range(len(nums)):
        result.append(nums[i] + nums[i-1])

    return result