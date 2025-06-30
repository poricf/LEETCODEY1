class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        arr = list(set(nums))
        ans = 0
        arr.sort()
        for num in arr:
            if num + 1 in count:
                ans = max(ans , count[num] + count[num + 1])
        
        return ans