#include <iostream>
#include <vector>
#include <queue>

int lastStoneWeight(std::vector<int>& stones) {
    // Max heap
    std::priority_queue<int> stoneHeap(std::less<int>(), stones);

    while (stoneHeap.size() > 1) {
        int strongestStone = stoneHeap.top();
        stoneHeap.pop();
        
        int secondStrongestStone = stoneHeap.top();
        stoneHeap.pop();
        
        int resultedStone = strongestStone - secondStrongestStone;

        if (resultedStone) stoneHeap.push(resultedStone);
    }

    if (stoneHeap.size() > 0) return stoneHeap.top();
    else return 0;
}

/*
    Max heaps help us keep track of the largest elements,
    so poping the largest two, and pushing back their difference
    will eventually result in reducing the stones to one, or zero.
*/