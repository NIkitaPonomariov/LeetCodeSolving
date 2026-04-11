class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        #value its what we need remove
        k: int = 0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[k] = nums[x]
                k += 1
            elif nums[x] == val:
                continue
        
        return k