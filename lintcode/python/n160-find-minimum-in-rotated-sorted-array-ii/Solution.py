class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        zip_array = zip(num[: -1], num[1:])
        min_value = [a for a in zip_array if a[0] > a[1]]
        if len(min_value) == 0:
            return num[0]
        else:
            return min_value[0][1]

if __name__ == '__main__':
    assert Solution().findMin([1, 1, -1, 1]) == -1
