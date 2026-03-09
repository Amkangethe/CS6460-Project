def running_sum(nums: list[int]) -> list[int]:
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result