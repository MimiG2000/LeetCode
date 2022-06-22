class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #brute force < hashmap 
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ret = nums[i] + nums [j]
                if ret == target: 
                    return list((i,j))
      