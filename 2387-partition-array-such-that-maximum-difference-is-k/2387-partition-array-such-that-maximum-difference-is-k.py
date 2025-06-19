class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        first = nums[0]
        ans = 1
        for i in range(1 , n):
            if nums[i] - first > k:
                first = nums[i]
                ans += 1
        
        return ans
            

