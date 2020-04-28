# First Attempt: Time Limit Exceeded
import heapq

class Node(object):
    def __init__(self, id: int, val: int):
        self.val = val
        self.id = id

    def __repr__(self):
        return f'Node value: {self.val}'

    def __lt__(self, other):
        return self.id < other.id
    
    def __eq__(self, val):
        return self.val == val


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.duplicates = set()
        self.unique_heap = list()
        self.unique_set = set()
        self.id = -1
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.unique_heap:
            return self.unique_heap[0].val
        return -1

    def add(self, value: int) -> None:
        if value not in self.duplicates:
            if value in self.unique_set:
                self.unique_heap.remove(value)
                self.unique_set.remove(value)
                heapq.heapify(self.unique_heap)
                self.duplicates.add(value)
            else:
                newNode = Node(self.getId(), value)
                heapq.heappush(self.unique_heap, newNode)
                self.unique_set.add(value)

    def getId(self):
        self.id += 1
        return self.id


##########################################################################


# Second Attempt: Accepted
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = list()
        self.num_count = dict()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1

    def add(self, value: int) -> None:
        if value in self.num_count:
            self.num_count[value] += 1
            while (self.queue and self.num_count[self.queue[0]] > 1):
                self.queue.pop(0)
        else:
            self.num_count[value] = 1
            self.queue.append(value)
