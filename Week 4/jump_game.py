from typing import List

# First Attempt: Time Limit Exceeded
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.recursiveJump(nums, 0)
    
    def recursiveJump(self, nums: List[int], index: int) -> bool:
        if index == len(nums)-1:
            return True
        elif index > len(nums)-1:
            return False
        else:
            return self.jumpAllPossible(nums, index)

    def jumpAllPossible(self, nums: List[int], index: int) -> bool:
        result = False
        for i in range(nums[index]):
            result = result or self.helper(nums, index+i+1)
        return result

# Simply try all possible moves, and see wether any of them
# reaches the last index. 


#####################################################################


# Second Attempt: Acceptped    
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for index in range(len(nums))[::-1]:
            if index + nums[index] >= goal:
                goal = index
        return True if goal == 0 else False

# Start from the last index, and keep track of the last index
# that still has a path to the goal, if the last index ended up
# being the first one, then there is a possible solution.