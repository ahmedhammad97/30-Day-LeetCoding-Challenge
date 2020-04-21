#include <vector>
#include <algorithm>

// This is the BinaryMatrix's API interface.
// You should not implement it, or speculate about its implementation
class BinaryMatrix {
  public:
    int get(int x, int y);
    std::vector<int> dimensions();
};


class Solution {
public:
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        int minOne = std::pow(2, 30);
        for (int i = 0; i < binaryMatrix.dimensions()[0]; i++) {
            int oneIndex = binarySearch(binaryMatrix, i);
            if (oneIndex != -1) minOne = std::min(oneIndex, minOne);
        }
        return minOne == std::pow(2, 30) ? -1 : minOne;
    }
    
    
    int binarySearch(BinaryMatrix &binaryMatrix, int row) {
        int left = 1;
        int right = binaryMatrix.dimensions()[1]-1;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            int midValue = binaryMatrix.get(row, mid);

            if (midValue == 1 && binaryMatrix.get(row, mid-1) == 0)
                return mid;

            if (midValue == 0)
                left = mid + 1;

            else
                right = mid - 1;
        }
        
        return (binaryMatrix.get(row, 0))-1;
    }
};


/*
    The solution is simple as doing a binary search for every row,
    and returning the least occurrence of a one that percedes
    a zero, or -1 if none is found.
*/