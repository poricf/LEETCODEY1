class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        # dp[i][j] -> the longset subsequence in t[:i] s[:j]
        M = len(s) + 1
        N = len(t) + 1
        dp = [[0] * M for _ in range(N)]

        for i in range(1 , N):
            for j in range(1 , M):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    without_s = dp[i][j - 1]
                    without_t = dp[i - 1][j]
                    dp[i][j] = max(without_s , without_t)
        
        return dp[-1][-1]