class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        maxs = [-1] * n
        mx = -1
        for i in range(n - 1 , -1 , -1):
            mx = max(nums[i] , mx)
            maxs[i] = max(nums[i] , mx)
        
        ans = -1
        for i in range(n):
            ans = max(maxs[i] - nums[i] , ans)
        
        return ans if ans > 0 else -1

