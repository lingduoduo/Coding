from  collections import Counter
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        d = Counter()
        curr = 0
        res = 0

        for r in range(len(nums)):
            d[nums[r]] += 1
            curr += nums[r]
            while d[nums[r]] > 1 or (r - l + 1) > k:
                curr -= nums[l]
                d[nums[l]] -= 1
                l += 1
            if (r - l + 1) == k:
                res = max(res, curr)
        return res

if __name__ == "__main__":
    res = Solution().maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3)
    print(res)



