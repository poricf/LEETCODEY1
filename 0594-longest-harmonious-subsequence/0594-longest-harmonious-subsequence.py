class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = 0
        window = defaultdict(int)
        ans = 0
        print(nums)
        while left < n and  right < n:
            while right < n and (nums[right] == nums[left] or nums[right] - 1 == nums[left]):

                window[nums[right]] += 1
                right += 1
            if len(window) == 2:
                ans = max(ans , right - left)
            
        
            
            val = nums[left]
            while left < n and nums[left] == val:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
        return ans

