class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

# For python3, `reduce` has to be imported from `functools`

# The basic idea is that XORing two similar integers yeilds zero,
# so XORing the whole list will cancel out all the duplicates,
# leaving us with the desired integer
