class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for i in range(n + 1)]

        if s[0] == '0': return 0
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] in '12':
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0
            else:
                if s[i - 1] == '1' or (s[i - 1] == '2' and 1 <= int(s[i]) <= 6):
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]

        return dp[-1]


    