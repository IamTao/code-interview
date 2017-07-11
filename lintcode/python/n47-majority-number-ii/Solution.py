class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        candidate_1, candidate_2 = None, None
        count_1, count_2 = 0, 0

        for num in nums:
            if candidate_1 == num:
                count_1 += 1
            elif candidate_2 == num:
                count_2 += 1
            elif count_1 == 0:
                candidate_1 = num
                count_1 += 1
            elif count_2 == 0:
                candidate_2 = num
                count_2 += 1
            else:
                count_1 -= 1
                count_2 -= 1

        count_1, count_2 = 0, 0
        for num in nums:
            if candidate_1 == num:
                count_1 += 1
            elif candidate_2 == num:
                count_2 += 1
        return candidate_1 if count_1 > count_2 else candidate_2
