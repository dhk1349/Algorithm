class Solution:
    def trap(self, height: List[int]) -> int:
        beg=-1
        left_wall=0
        right_wall=0
        cnt=0
        length=len(height)
        if len(height)<=1:
            return 0
        for idx, elem in enumerate(height):
            if elem is not 0:
                beg=idx
                left_wall=height[beg]
                right_wall=max(height[beg+1:])
                break
        height.append(0)
        for idx in range(beg+1, length):
            print(f"at {idx}, {(min(left_wall, right_wall)-height[idx])} added")
            cnt+=max(min(left_wall, right_wall)-height[idx], 0)
            left_wall=max(left_wall, height[idx])
            right_wall=max(height[idx+1:])
        return cnt
        
        """
        too inefficient
        #find highest block
        #count water block from the 1st floor.
        if len(height)==0:
            return 0
        hi=max(height)
        cnt=0
        for i in range(hi):
            beg=False
            for i in range(len(height)-1, -1, -1):#last block of the layer
                if height[i] is not 0:
                    end=i
                    break
            for idx, elem in enumerate(height):
                if elem is not 0 and beg is False:
                    beg=True #first block of the layer
                if elem is 0 and beg is True and idx<=end:
                    cnt+=1
            
            #subtract 1    
            for i in range(len(height)):
                if height[i]>0:
                    height[i]-=1
        
        return cnt
        """
