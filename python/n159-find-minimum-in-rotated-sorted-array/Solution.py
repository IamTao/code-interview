class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
	  	result = [tup[1] for tup in zip(num[:-1], num[1:]) if tup[0] > tup[1]]
	  	if len(result) == 1:
	  		return result[0]
	  	else:
	  		return num[0]


if __name__ == '__main__':
	x = [6,1,2,3,4,5]
	assert Solution().findMin(x) == 1