class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # return self.climbStairs_tle(n)
        # return self.climbStairs_dp(n)
        return self.climbStairs_fi(n)

    sol = {0: 1, 1: 1, 2: 2}
    def climbStairs_dp(self, n):
        if n in Solution.sol.keys():
            return Solution.sol[n]
        else:
            tmp = Solution.sol.get(n - 1, self.climbStairs_dp(n - 1)) + Solution.sol.get(n - 2, self.climbStairs_dp(n - 2))
            Solution.sol[n] = tmp
            return tmp

    def climbStairs_fi(self, n):
        # write your code here
        if n <= 0:
            return 1
        x = [1, 2]
        for i in xrange(n):
        	x += [reduce(lambda a, b: a + b, x[-2:]), ]
        return x[n - 1]

    def climbStairs_tle(self, n):
        # write your code here
        if n == 0:
            return 1
        if n < 0:
            return 0
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

if __name__ == '__main__':
    Solution().climbStairs(3)
    Solution().climbStairs(2)
    Solution().climbStairs(5)
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(5) == 8
