from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        reduced_shift = self.reduceShifts(shift)
        return self.shifter(s, reduced_shift)


    def reduceShifts(self, shifts: List[List[int]]) -> List[int]:
        left_shift_accumulator = 0
        for shift in shifts:
            if (shift[0] == 0):
                left_shift_accumulator += shift[1]
            else:
                left_shift_accumulator -= shift[1]
        
        direction = self.deduceDirection(left_shift_accumulator)
        return [direction, abs(left_shift_accumulator)]


    def deduceDirection(self, accumulator: int) -> int:
        return 0 if accumulator > 0 else 1

    
    def shifter(self, s: str, shift: List[int]) -> str:
        shiftValue = shift[1] % len(s)
        if (shift[0] == 0):
            return self.leftShifter(s, shiftValue)
        else:
            return self.rightShifter(s, shiftValue)

    
    def rightShifter(self, s: str, amount: int) -> str:
        shift_index = len(s) - amount 
        return s[shift_index:] + s[:shift_index]
    

    def leftShifter(self, s: str, amount: int) -> str:
        shift_index = amount 
        return s[shift_index:] + s[:shift_index]


# 1- Reduce all shifts into one shift
# 2- Deduce the accumulated shift direction
# 3- Calculate the mod of the shift divided
# by the length (in case of big shift values)
# 4- return the shifted string