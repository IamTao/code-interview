class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        c = a ^ b
        cnt = 0
        for i in range(32):
            if c & (1 << i) != 0:
                cnt += 1
        return cnt

if __name__ == '__main__':
    Solution().bitSwapRequired(31, 14)
