def dedupe(nums: list[int]) -> list[int]:

    if len(nums) == 0:
        return []
    
    nums.sort()
    nums_copy = []
    
    
    index = 0
    
    for i in range(1, len(nums)):
        if(nums[index] != nums[i]):
            nums_copy.append(nums[i])
        
        index+=1
    
    print(nums_copy)
    return nums_copy
            

