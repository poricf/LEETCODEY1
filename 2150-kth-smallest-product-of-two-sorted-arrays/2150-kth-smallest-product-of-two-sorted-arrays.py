class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def check(mid):
            cnt = 0
            for num in nums1:
                if num == 0:
                    if mid >= 0:
                        cnt += len(nums2)
                elif num > 0:
                    ind = bisect_right(nums2 , mid / num)
                    cnt += ind
                else:
                    ind = bisect_left(nums2 , mid / num)
                    cnt += len(nums2) - ind
            return cnt >= k

        left = -10**10 - 10
        right = 10**10 + 10
        ans = 0
        while left <= right:
            mid = (left + right)//2
            if check(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        
        return ans
