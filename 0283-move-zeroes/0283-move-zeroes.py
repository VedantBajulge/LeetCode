class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_last = 0 
        for i in range (len(nums)):
            if nums[i] != 0:
                nums[insert_last],nums[i]=nums[i],nums[insert_last]
                insert_last += 1