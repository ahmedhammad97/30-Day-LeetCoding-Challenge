#include <vector>
#include <algorithm>

void moveZeroes(std::vector<int>& nums) {
    int nonZeroCounter = 0;

    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            nums[nonZeroCounter] = nums[i];
            nonZeroCounter++;
        }
    }

    while (nonZeroCounter < nums.size())
        nums[nonZeroCounter++] = 0;
}


/*
    The typical nested-loop solution would take O(n^2),
    the same for the two-pointers approach.
    So, the optimal solution is to keep a count of the non-zero
    elements, and place every non-zero element in the index of
    the counter. It is either that the number will replace itself,
    or replace a zero. A final step would be to append the remaining
    zeros to the end of the array. This runs in O(n)
*/