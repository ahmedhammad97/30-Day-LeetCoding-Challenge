from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = self.leftProductScan(nums)
        right_product = self.rightProductScan(nums)
        return [left * right for left, right in zip(left_product, right_product)]

    
    def leftProductScan(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
        return left_product

    
    def rightProductScan(self, nums: List[int]) -> List[int]:
        right_product = [1] * len(nums)
        for i in range(len(nums) - 1)[::-1]:
            right_product[i] = right_product[i+1] * nums[i+1]
        return right_product

# Using division is not allowed!

# The naive approach is to scan the list once, and for every element,
# calculate the product of all the elements in the list except it.
# However, this approach takes O(N^2).

# A good modification is to cache the products at every element, once
# for all the element on the right, and other for the elements on the left.
# So that, for every element, the resulted product is the product of
# the cached left value and the right cached value.
# This runs in O(N), with O(N) of space.

# We can modify further more to store cached values in the result list
# directly, but it becomes very hard to follow. Does not worth the mess.