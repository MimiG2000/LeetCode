class Solution:
    #   naive approach: 
    #   -use only bricks
    #   -store values in a queue (or heap...something sorted)
    #   -if bricks are depleted use ladder for the highest difference
    #   -add bricks
    #   -repeat till no ladders are remaining
    
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        l = len(heights)
        h = []
        
        for i in range(l-1):
            diff =  heights[i+1] - heights[i] 
            
            if diff > 0:
                
                if bricks >= diff:              #use bricks
                    heapq.heappush(h,-1*diff)   #add diff to heap (muliply by -1 for "max_heap")
                    bricks -= diff
            
                elif bricks < diff and ladders: #not enough bricks -> use ladders and add bricks
                    
                    if len(h) == 0:
                        ladders -= 1            #no heap
                           
                    else:
                        if diff > (h[0]*-1):         #use ladder for current building 
                            ladders -= 1
                            continue
                        
                        bricks += heapq.heappop(h)* -1          #biggest diff
                        ladders -= 1
                        
                        if bricks >= diff:
                            heapq.heappush(h,-1*diff)
                            bricks -= diff                      #use for current building bricks
                        
                        else:
                            return i
                               
                elif bricks < diff and ladders == 0:    #no rescources left 
                    return i
            
                
        return l-1                                      #climbed all buildings
                
                
                
                
            
        
    
        
        
        
        