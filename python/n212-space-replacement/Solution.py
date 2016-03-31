class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        ind = 0
        while ind < length:
        	if string[ind] == " ":
	        	string.append("")
	        	string.append("")
	        	length += 2
	        	for j in xrange(length - 1, ind, -1):
	        		string[j] = string[j - 2]

	        	string[ind: ind + 3] = list("%20")
	        	ind += 2
	        ind += 1
		return length

class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        replaced = list(reduce(lambda a, b: a + b, ["%20" if i == " " else i for i in string]))
        return len(replaced)

if __name__ == '__main__':
	test = Solution()
	test.replaceBlank(list("Mr John Smith"), 13) == 17


