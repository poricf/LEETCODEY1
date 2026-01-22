class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        st = []
        prev = -1
        def check(arr):
            for i in range(1 , len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True
        cnt = 0
        while nums:
            # print(nums)
            if check(nums):
                return cnt
            mn = float("inf")
            for i in range(1 , len(nums)):
                sm = nums[i] + nums[i-1]
                if sm < mn:
                    ind = i
                    mn = sm

            x = nums.pop(ind)
            nums[ind-1] += x
            cnt += 1

        return cnt