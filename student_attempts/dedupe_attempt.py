def dedupe(nums: list[int]) -> list[int]:

    result = []

    for i in range(len(nums)):
        if nums[i] not in result:
            result.append(nums[i])

    return result[1:]