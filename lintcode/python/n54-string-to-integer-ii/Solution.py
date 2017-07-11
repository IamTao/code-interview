class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        # write your code here
        if len(str) == 0:
            return 0
        sign, num, pointer = False, 0, 0
        int_max, int_min = (1 << 31) - 1, - (1 << 31)
        while str[pointer] == ' ':
            pointer += 1
        if str[pointer] == '-' or str[pointer] == '+':
            sign = True if str[pointer] == '-' else False
            pointer += 1
        while pointer < len(str) and str[pointer] >= '0' and str[pointer] <= '9':
            num = num * 10 + ord(str[pointer]) - ord('0')
            x = -num if sign else num
            if x > int_max:
                return int_max
            if x < int_min:
                return int_min
            pointer += 1
        return -num if sign else num
