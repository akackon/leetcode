from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_dict = {}
    for count,value in enumerate(nums):
        diff = target - value
        if diff in nums_dict:
            return [count,nums_dict[diff]]
        nums_dict[value] = count

print(twoSum([3,2,4],6))