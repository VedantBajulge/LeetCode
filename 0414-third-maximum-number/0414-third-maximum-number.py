class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums=set(nums)
        if len(nums)<3:
            return max(nums)
        else:
           
            f_max=max(nums)
            nums.remove(f_max)
            s_max=max(nums)
            nums.remove(s_max)

            return max(nums)

        