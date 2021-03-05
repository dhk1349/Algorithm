from copy import deepcopy
class Solution:
    def __init__(self):
        self.resultlst=[]
    def permute(self, nums: List[int]) -> List[List[int]]:
        copylst=[]
        for i in range(len(nums)):
            copylst=deepcopy(nums)
            copylst.remove(nums[i])
            self.create(copylst, [nums[i]])
        return self.resultlst
    
    def create(self, nums, lst):
        # recursive
        # 
        
        if len(nums)==0:
            #print(f"nums len is 0, lst:{lst}, resultlst: {self.resultlst}")
            self.resultlst.append(lst)
            return
        
        for i in range(len(nums)):
            copylst=deepcopy(nums)
            copylst.remove(nums[i])
            
            _lst=deepcopy(lst)
            _lst.append(nums[i])
            #print(f"recursive create call {nums}, {copylst}, {_lst}, {self.resultlst}")
            self.create(copylst, _lst)
            
