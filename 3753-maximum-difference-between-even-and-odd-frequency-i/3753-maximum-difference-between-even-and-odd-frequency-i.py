class Solution:
    def maxDifference(self, s: str) -> int:
        cc = Counter(s)
        mxodd = 0 
        mneven = len(s)
        for v in cc.values():
            if v % 2 == 0:
                mneven = min(v , mneven)
            else:
                mxodd = max(v , mxodd)
        
        return mxodd - mneven
