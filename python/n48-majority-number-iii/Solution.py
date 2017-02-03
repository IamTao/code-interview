class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        counts = {}
        max = 0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > max:
                max = counts[num]
                majority = num
        return majority
