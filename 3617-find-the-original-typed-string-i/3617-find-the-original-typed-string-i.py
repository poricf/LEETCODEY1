class Solution:
    def possibleStringCount(self, word: str) -> int:
        '''
        ab
        '''
        n = len(word)
        cnt = 1
        ans = 1
        for i in range(1 ,n):
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                ans += (cnt - 1)
                cnt = 1
        ans += (cnt - 1)
        return ans
