class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        smaller=True
        for idx, elem in enumerate(nums):
            if target==elem:
                return idx
            elif target<elem:
                return idx
            
        return len(nums)
