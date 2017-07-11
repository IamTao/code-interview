class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        x = [0, 1]
        for i in xrange(n):
        	x += [reduce(lambda a, b: a + b, x[-2:]), ]
        return x[n - 1]


if __name__ == '__main__':
	assert Solution().fibonacci(1) == 0
	assert Solution().fibonacci(2) == 1
	assert Solution().fibonacci(3) == 1
	assert Solution().fibonacci(4) == 2
	assert Solution().fibonacci(5) == 3
	assert Solution().fibonacci(40) == 63245986

