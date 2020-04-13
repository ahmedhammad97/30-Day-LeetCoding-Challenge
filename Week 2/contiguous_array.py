def findMaxLength(self, nums: List[int]) -> int:
    accumulator = 0
    max_length = 0
    history_dict = dict({0: -1})
    for index, num in enumerate(nums):
        accumulator += 2 * num - 1
        
        if accumulator in history_dict:
            curr_length = index - history_dict[accumulator]
            max_length = max(max_length, curr_length)
        else:
            history_dict[accumulator] = index
    
    return max_length


# The basic idea is to accumulate the zeros and ones as we
# scan the list, when the accumulator is zero again, this means
# we have a sub-list of equal zeros and ones, but this only works
# for sub-lists starting from the beginning of the list.

# To make it work for every sub-list we gotta check for "relative"
# differences instead.

# If we hit an accumulated value that we hit before, this means
# there's a target sub-list between these two similar indices.

# Now what's left is to keep track of the maximum length of all 
# these target sub-lists.