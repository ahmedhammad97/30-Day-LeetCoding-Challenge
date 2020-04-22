from typing import List

# First Attempt: Time Limit Exceeded
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            curr_sum = 0
            for end in range(start, len(nums)):
                curr_sum += nums[end]
                if (curr_sum == k):
                    count += 1
        return count

###########################################################

# Second Attempt: Accepted
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = curr_sum = 0
        num_dict = dict([(0, 1)])
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum - k in num_dict:
                count += num_dict[curr_sum - k]
            num_dict.update({curr_sum: num_dict.get(curr_sum, 0) + 1})
        return count
