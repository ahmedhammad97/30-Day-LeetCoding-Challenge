class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr_max = nums[0]

        for num in nums[1:]:
            curr_max = max(curr_max + num, num)
            max_so_far = max(max_so_far, curr_max)

        return max_so_far


# Kadane’s algorithm is by far the optimal solution to the
# maximum subarray problem, it compares the `curr_max` with
# the `best_max_so_far`, and sets the prior to the maximum
# of both.
#
# Another common divide and conquer approach, recursively
# calculates:
#   a) the maximim left subarray
#   b) the maximum right subarray
#   c) the maximum subarray containing the midpoint
# and returns the maximim of all three.
