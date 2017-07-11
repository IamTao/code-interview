class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if not bool(strs):
            return ""
        count = 0
        label = True
        while label:
            for ind, str in enumerate(strs):
                if len(str) == count:
                    label = False
                    break
                if ind == 0:
                    current = str[count]
                elif str[count] != current:
                    label = False
            if label:
                count += 1
        return strs[0][: count]

if __name__ == '__main__':
    # assert Solution().longestCommonPrefix(["ABCD", "ABEF", "ACEF"]) == "A"
    # assert Solution().longestCommonPrefix(["ABCDEFG", "ABCEFG", "ABCEFA"]) == "ABC"
    # assert Solution().longestCommonPrefix([]) == ""
    assert Solution().longestCommonPrefix(["ABC"]) == "ABC"
