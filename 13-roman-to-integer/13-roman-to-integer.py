class Solution(object):
    
    def romanToInt(self, s):
        counter = 0
        """
        :type s: str
        :rtype: int
        """
        for i in range(0, len(s)): 
            
            if s[i] == 'I':
                
                if i+1 < len(s) and (s[i+1] == 'V' or s[i+1] == 'X'):
                    counter -= 1
                    continue
                else: 
                    counter += 1
                        
            elif s[i] == 'V':
                counter += 5
                
            elif s[i] == 'X':
                
                if i+1 < len(s) and (s[i+1] == 'C' or s[i+1] == 'L'):
                    counter -= 10
                    continue
                    
                else:
                    counter += 10
                    
            elif s[i] == 'L':
                counter += 50
                
                
                
            elif s[i] == 'C':
                
                if i+1 < len(s) and (s[i+1] == 'D' or s[i+1] == 'M'):
                    counter -= 100
                    continue
                    
                else:
                    counter += 100
            
            elif s[i] == 'D':
                counter += 500
                
            elif s[i] == 'M':
                counter += 1000
                
                
    
        return counter
        