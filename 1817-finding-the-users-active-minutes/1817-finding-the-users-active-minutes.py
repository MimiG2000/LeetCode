class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
       
        n = len(logs)
        ans = [0]* k
        s = collections.defaultdict(set)        #defaultdict with sets as values
        
        for log_id, log_minu in logs:
            s[log_id].add(log_minu)
            
        for log_id in s:
            
            l = len(s[log_id]) - 1      #uam position 
            ans[l] += 1
                    
        return ans
            
            
            
        
        
            
                
                
        
        
        
        
            
            
                
                
                
        