class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def check(mid):
            i = 1
            cnt = 0
            while i < len(nums):
                if nums[i] - nums[i - 1] <= mid:
                    i += 2
                    cnt += 1
                else:
                    i += 1
            
            return cnt >= p
        

        left = 0
        right = nums[-1] - nums[0]
        ans = float("inf")
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = min(mid , ans)
                right = mid - 1
            else:
                left = mid + 1
       
        return ans
                

