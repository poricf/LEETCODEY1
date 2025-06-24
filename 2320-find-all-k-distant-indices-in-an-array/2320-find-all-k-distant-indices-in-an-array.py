class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = []
        n = len(nums)
        pref = [0] * (n + k + 1)
        for i , num in enumerate(nums):
            if num == key:
                key_indices.append(i)
                pref[max(0 , i - k)] += 1
                
                pref[min(n , i + k + 1)] -= 1
        ans = []
        marked = list(accumulate(pref))
        for i , val in enumerate(marked):
            if val: ans.append(i)
        
        return ans

            
            
        
        