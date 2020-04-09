def backspaceCompare(S: str, T: str) -> bool:
    stack_s = addCharsToStack(S)
    stack_t = addCharsToStack(T)
    return stack_s == stack_t

def addCharsToStack(string: str) -> list:
    stack = list()
    for char in string:
        if char == '#':
            stack.pop() if stack != [] else pass
        else :
            stack.append(char)
    return stack

# Stacks are very good with canceling chars,
# so if we added both strings to stacks, and cancel out
# elements preceded by `#`, both stacks should end up
# having the same values.

# A solution with constant space exists.