import statistics as st

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        counter = 0
        med = median(nums)
        print(med)
        
        rounded_med = round(med)
        
        for n in nums:
            
            i = abs(n - med)
            counter += i
            
        return int(counter)
            
        