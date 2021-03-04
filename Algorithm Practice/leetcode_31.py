class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        _reversed=False
        window=2
        cursor=-1
        if(len(nums)==1):
            return
        while window!=len(nums)+1:
            for i in range(window-1):
                if nums[cursor-(i+1)]<nums[cursor-i]: #not reverserd
                    for j in range(-1, cursor-(i+1), -1):
                        if nums[j]>nums[cursor-(i+1)]:
                            swap=nums[cursor-(i+1)]
                            nums[cursor-(i+1)]=nums[j]
                            nums[j]=swap
                            nums[cursor-(i):]=sorted(nums[cursor-(i):])
                            return
            window+=1

                
        nums.sort()
