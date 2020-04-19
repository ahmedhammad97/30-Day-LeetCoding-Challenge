#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int pivot = findArrayShift(nums, 0, nums.size()-1);
        
        if (pivot == -1) return binarySearch(nums, 0, nums.size()-1, target);
        if (nums[pivot] == target) return pivot;

        if (nums[0] <= target) return binarySearch(nums, 0, pivot-1, target);
        else return binarySearch(nums, pivot+1, nums.size()-1, target);
    }


    int findArrayShift(std::vector<int>& nums, int low, int high) {
        if (high < low) return -1;
        if (high == low) return low;

        int mid = (low + high)/2;
        if (mid < high && nums[mid] > nums[mid + 1])
            return mid;

        if (mid > low && nums[mid] < nums[mid - 1])
            return (mid-1);

        if (nums[low] >= nums[mid])
            return findArrayShift(nums, low, mid-1);

        return findArrayShift(nums, mid + 1, high);
    }


    int binarySearch(std::vector<int>& nums, int left, int right, int target) {
        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target)
                return mid;

            if (nums[mid] < target)
                left = mid + 1;

            else
                right = mid - 1; 
        } 
        return -1; 
    }
};

/*
    Find the pivot point where the shift starts.
    Depending on the pivot's position, we only 
    search on the side that might contain the target.
    
    This runs in O(logN) with no extra space.
*/