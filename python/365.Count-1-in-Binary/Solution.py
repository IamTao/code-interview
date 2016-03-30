# -*- coding: utf-8 -*-

class Solution:
    # @param num: an integer (binary)
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        return self.countOnes4(num) # 398 ms
        
    def countOnes2(self,num):
    	if num < 0:
    		num = (1 << 32) + num
        count = 0
        while num != 0:
            count += num & 0x01
            num = num >> 1
        return count

	# 利用位运算
	# 这个32位数与0000 0001 与运算的值是1，记录1的个数

    def countOnes3(self,num):
    	if num < 0:
    		num = (1 << 32) + num
        count = 0
        while num != 0:
            num = num & (num - 1)
            count += 1
        return count

    def countOnes4(self, num):
    	if num < 0:
    		num = (1 << 32) + num
    	num = bin(num)[2: ]
    	return len([i for i in list(num) if i == "1"])

if __name__ == '__main__':
	assert Solution().countOnes(32) == 1
	assert Solution().countOnes(5) == 2
	assert Solution().countOnes(1023) == 10
	assert Solution().countOnes(-1) == 32