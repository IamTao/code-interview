class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        len_nums = len(nums)

        if len_nums == 0 or len_nums == 1:
            return [0, 0]
        records = {}

        sum = 0
        for ind, val in enumerate(nums):
            sum += val

            if sum in records:
                return [records[sum] + 1, ind]
            else:
                records[sum] = ind
        sums = list(records.keys())
        sorted_sums = sorted(sums)
        sorted_sums_diff = [(ind, abs(sorted_sums[ind] - sorted_sums[ind + 1]))
                            for ind in range(len_nums - 1)]
        min_sum_diff = min(sorted_sums_diff, key=lambda x: x[1])[0]
        start_sum, end_sum \
            = sorted_sums[min_sum_diff], sorted_sums[min_sum_diff + 1]
        start_index, end_index = records[start_sum], records[end_sum]

        if start_index > end_index:
            return [end_index + 1, start_index]
        else:
            return [start_index + 1, end_index]


if __name__ == '__main__':
    print(Solution().subarraySumClosest([-3, 1, 1, -3, 5]))
    print(Solution().subarraySumClosest([5, 10, 5, 3, 2, 1, 1, -2, -4, 3]))
