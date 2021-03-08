from copy import deepcopy
class Solution:
    #recursively find answer
    def __init__(self):
        self.answer=[]
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        for idx, elem in enumerate(candidates):
            container=[elem]
            if elem==target:
                self.answer.append([elem])
            else:
                self.recursive_module(candidates[idx:], target, container)
        
        return self.answer
    
    def recursive_module(self, candidates, target, container):
        #print(f"recursive call: {candidates}, {target}, {container}")
        for idx, elem in enumerate(candidates):
            _container=deepcopy(container)
            _container.append(elem)
            #print(f"{sum(_container)} and {target}")
            if sum(_container)<target:
                self.recursive_module(candidates[idx:], target, _container)
                
            elif sum(_container)==target:
                self.answer.append(_container)
            #else: do nothing
