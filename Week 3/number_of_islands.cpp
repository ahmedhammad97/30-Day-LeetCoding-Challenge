#include <vector>
#include <unordered_set>
#include <queue>

class Solution {
private:
    struct pair_hash {
        inline std::size_t operator()(const std::pair<int,int> & v) const {
            return v.first*31+v.second;
        }
    };
    std::unordered_set< std::pair<int, int>,  pair_hash> unvisited;
    
public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        int counter = 0;
        initializeUnvisitedSet(grid);
        while(!unvisited.empty()) {
            std::pair<int,int> currCell = *(unvisited.begin());
            if (grid[currCell.first][currCell.second] == '1') {
                counter++;
                clearIsland(grid, std::make_pair(currCell.first, currCell.second));
            }
        }
        return counter;   
    }


    void initializeUnvisitedSet(std::vector<std::vector<char>>& grid) {
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                unvisited.insert(std::make_pair(i, j));
            }
        }
    }
    
    void clearIsland(std::vector<std::vector<char>>& grid, std::pair<int, int> cell) {
        std::queue<std::pair<int, int>> cellQueue;
        cellQueue.push(cell);
        
        while(cellQueue.size()) {
            std::pair<int, int> currCell = cellQueue.front();
            cellQueue.pop();
            grid[currCell.first][currCell.second] = '0';
            unvisited.erase(currCell);
            
            // Sorry for this mess .. couldn't do better :$
            if (currCell.first > 0 && grid[currCell.first-1][currCell.second] == '1')
                cellQueue.push(std::make_pair(currCell.first-1, currCell.second));
            
            if (currCell.second > 0 && grid[currCell.first][currCell.second-1] == '1')
                cellQueue.push(std::make_pair(currCell.first, currCell.second-1));
            
            if (currCell.first+1 < grid.size() && grid[currCell.first+1][currCell.second] == '1')
                cellQueue.push(std::make_pair(currCell.first+1, currCell.second));
            
            if (currCell.second+1 < grid[0].size() && grid[currCell.first][currCell.second+1] == '1')
                cellQueue.push(std::make_pair(currCell.first, currCell.second+1));
                
        }
    }
};

/*
    I started with a simple scan to every grid cell, and for each
    '1' I find, I increment a counter, then change it to '0' alongside
    with all it's '1' neighbors using Breadth First Search.
    This however exceeds the runtime limit.

    So, a workaround would be to have a hash set tracking every unvisited
    cell, and we only scan those unvisited instead of the whole grid.
    This guarantees a O(M*N) scan, with O(N) extra space.

    A constant-space approach exists.
    
*/