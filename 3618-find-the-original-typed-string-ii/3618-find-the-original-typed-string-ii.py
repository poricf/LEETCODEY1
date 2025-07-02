class Solution:
    MOD = 10**9 + 7
    
    def possibleStringCount(self, word: str, k: int) -> int:
        # Step 1: Extract run lengths
        freq = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                freq.append(count)
                count = 1
        freq.append(count)
        
        total_runs = len(freq)
        max_len = sum(freq)
        
        # If max_len < k, no strings of length >= k
        if max_len < k:
            return 0
        
        # If total runs >= k, then minimal length is at least k
        if total_runs >= k:
            # The number of possible strings is product of freq[i]
            res = 1
            for x in freq:
                res = (res * x) % self.MOD
            return res
        
        # Step 2: DP f[i][j] optimized to 1D array
        dp = [0] * (k)
        dp[0] = 1  # base case: empty string
        
        for i, length in enumerate(freq):
            prefix = [0] * (k)
            prefix[0] = dp[0]
            for j in range(1, k):
                prefix[j] = (prefix[j - 1] + dp[j]) % self.MOD
            
            new_dp = [0] * (k)
            for j in range(k):
                left = j - length
                if left - 1 >= 0:
                    new_dp[j] = (prefix[j - 1] - prefix[left - 1]) % self.MOD
                else:
                    new_dp[j] = prefix[j - 1] % self.MOD if j > 0 else 0
            
            dp = new_dp
        
        # Total number of strings = product of freq[i]
        total = 1
        for x in freq:
            total = (total * x) % self.MOD
        
        # sum of strings with length < k
        less_than_k = sum(dp) % self.MOD
        
        # Answer = total - less_than_k
        return (total - less_than_k) % self.MOD
