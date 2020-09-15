class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(1+len(s))

        dp[0] = 1

        for i in range(1, 1+len(s)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i != 1 and '10'<=s[i-2:i]<='26':
                dp[i] += dp[i-2]
        return dp[-1]