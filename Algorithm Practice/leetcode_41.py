class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        cnt=1
        for idx, elem in enumerate(nums):
            if elem<=0:
                continue
            elif cnt<elem:
                return cnt
            elif cnt==elem:
                cnt+=1
        return cnt
