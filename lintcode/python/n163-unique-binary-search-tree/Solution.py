class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        for ind in range(3, n + 1):
            dp.append(sum([dp[x] * dp[ind - x - 1] for x in range(ind)]))
        return dp[n]

if __name__ == '__main__':
    print(Solution().numTrees(3))
