class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        # dp[i][j] -> the longset subsequence in t[:i] s[:j]
        M = len(s) + 1
        N = len(t) + 1
        prev = [0] * M
        cur = [0] * M

        for i in range(1 , N):
            for j in range(1 , M):
                if s[j - 1] == t[i - 1]:
                    cur[j] = prev[j - 1] + 1
                else:
                    cur[j] = max(prev[j] , cur[j - 1])

            prev , cur = cur , [0] * M
        
        return prev[-1]