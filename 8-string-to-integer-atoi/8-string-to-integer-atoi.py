class Solution:
    def myAtoi(self, s: str) -> int:
        
        isnegative = False
        max = 2 ** 31 - 1
        min = -2 ** 31 
        
        #get rid of leading whitespaces
        s = s.strip()
         
        if s == '' or s == None:
            return 0
        
        #check sign
        if s[0] == '-':
            isnegative = True
            #s = s.replace('-','')
            s = s[1:]
            
        elif s[0] == '+':
            #s = s.replace('+','')
            s = s[1:]
            
        #check for words
        if s == '' or s[0] > '9' or s[0] < '0':
            return 0
        
        #search for pattern
        pattern = r'[0-9]*[.]?[0-9]*'           
        #result = re.search(pattern,s)
        finds = re.findall(pattern,s)
        
        result = finds[0]
        #no match
        if result == None:
            return 0
        
        #result = result.group()
        
        #float or int
        if('.' in result):
            result = float(result)
            result = int(result)
            
        else:
            result = int(result)
            
        # max value
        if result > max and not isnegative:
            return max
        
        elif result > max and isnegative:
            return min
        
        if isnegative:
            return result * -1
        else:
            return result
        
        return 0
        
    
        