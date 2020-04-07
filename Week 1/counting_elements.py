def countElements(arr) -> int:
    elementSet = set(arr)
    return sum(item + 1 in elementSet for item in arr)

# 1. Add all elements to a hashset
# 2. count elements whose increment exist in the hashset