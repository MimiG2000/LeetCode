class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str = ""
        
        while num > 0: 
            
            if num - 1000 >= 0:
                str += 'M'
                num -= 1000
            
            elif num - 900 >= 0:
                str += 'CM'
                num -= 900
                
            elif num - 500 >= 0:
                str += 'D'
                num -= 500
                
            elif num - 400 >= 0:
                str += 'CD'
                num -= 400
                
            elif num - 100 >= 0:
                str += 'C'
                num -= 100
             
            elif num - 90 >= 0:
                str += 'XC'
                num -= 90
                
            elif num - 50 >= 0:
                str += 'L'
                num -= 50
                
            elif num - 40 >= 0:
                str += 'XL'
                num -= 40
                
            elif num - 10 >= 0:
                str += 'X'
                num -= 10
                
            elif num - 9 >= 0:
                str += 'IX'
                num -= 9
                
            elif num - 5 >= 0:
                str += 'V'
                num -= 5
                
            elif num - 4 >= 0:
                str += 'IV'
                num -= 4
                
            elif num - 1 >= 0: 
                str += 'I'
                num -= 1
                        
        return str
            
        