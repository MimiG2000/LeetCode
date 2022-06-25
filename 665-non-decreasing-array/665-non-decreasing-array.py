class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        
        i = 0
        n = len(nums)
        flag = False
        
        for i in range(n-1):
            
            if nums[i] > nums[i+1]:
                
                if flag == True:
                    return False
                
                flag = True
                
                if i > 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
                    
        return True
                
                
        
        