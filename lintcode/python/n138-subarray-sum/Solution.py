class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        # return self.subarraySum_1(nums)
        return self.subarraySum_2(nums)

    def subarraySum_2(self, nums):
        hs = {0: -1}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in hs:
                return [hs[sum] + 1, i]
            hs[sum] = i
        return []

    # memory limit exceeded
    def subarraySum_1(self, nums):
        # write your code here
        n_row = len(nums)
        result = []

        for row in xrange(n_row):
            if row == 0:
                tmp = nums
            else:
                n_col = len(result[-1])
                tmp = [result[0][col] + result[row - 1][col + 1] for col in xrange(n_col - 1)]
            result += [tmp, ]

        return [[n_c, n_c + n_r] for n_r, row in enumerate(result) for n_c, col in enumerate(row) if col == 0][0]

if __name__ == '__main__':
    print Solution().subarraySum([-3, 1, 2, -3, 4])
