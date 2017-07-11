class Solution:
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        num = map(str, num)
        sorted_num = sorted(
            num,
            cmp=lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1)
        largest = ''.join(sorted_num)
        ind, length = 0, len(largest)
        while ind + 1 < length:
            if sorted_num[ind] != '0':
                break
            ind += 1
        return largest[ind:]


if __name__ == '__main__':
    Solution().largestNumber([1, 20, 23, 4, 8])
    Solution().largestNumber(
        [41, 23, 87, 55, 50, 53, 18, 9, 39, 63, 35,
         33, 54, 25, 26, 49, 74, 61, 32, 81, 97, 99,
         38, 96, 22, 95, 35, 57, 80, 80, 16, 22, 17,
         13, 89, 11, 75, 98, 57, 81, 69, 8, 10, 85,
         13, 49, 66, 94, 80, 25, 13, 85, 55, 12, 87,
         50, 28, 96, 80, 43, 10, 24, 88, 52, 16, 92,
         61, 28, 26, 78, 28, 28, 16, 1, 56, 31, 47,
         85, 27, 30, 85, 2, 30, 51, 84, 50, 3, 14,
         97, 9, 91, 90, 63, 90, 92, 89, 76, 76, 67, 55])
