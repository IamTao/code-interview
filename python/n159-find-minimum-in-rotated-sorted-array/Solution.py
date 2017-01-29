class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin_1(self, num):
        # write your code here
        result = [tup[1] for tup in zip(num[:-1], num[1:]) if tup[0] > tup[1]]
        if len(result) == 1:
            return result[0]
        else:
            return num[0]

    def findMin_2(self, num):
        # write your code here
        length = len(num)
        start, end = 0, length - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if num[mid] > num[end]:
                start = mid
            elif num[mid] < num[start]:
                end = mid
            else:
                return num[0]
        return min(num[start], num[end])

    def findMin_3(self, num):
        # write your code here
        length = len(num)
        start, end = 0, length - 1
        target = num[-1]
        while start + 1 < end:
            mid = (start + end) / 2
            if num[mid] <= target:
                end = mid
            else:
                start = mid
        return min(num[start], num[end])


if __name__ == '__main__':
    assert Solution().findMin_2([6, 1, 2, 3, 4, ]) == 1
    assert Solution().findMin_2([1, 2, 3]) == 1
