class Solution:
    def findLucky(self, arr: List[int]) -> int:
        unique = list(sorted(set(arr)))
        cc = Counter(arr)
        ans = -1
        for n in unique:
            if cc[n] == n:
                ans = n
        return ans
        
