class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        now = 0
        for index, el in enumerate(nums):
            now += el
            if now > max_num:
                max_num = now
            if now < 0:
                now = 0
        return max_num
            