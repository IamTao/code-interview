# For a given source string and a target string, you should output the first
# index(from 0) of target string in source string.
# If target does not exist in source, just return -1.


class Solution:
    def strStr(self, source, target): # O(n^2)
        # write your code here
        if source is None or target is None:
            return -1

        len_of_target = len(target)
        len_of_source = len(source)

        if len_of_target == 0:
            return 0
        if len_of_source == 0:
            return -1

        for start in xrange(len_of_source - len_of_target + 1):
            if source[start] == target[0]:
                for end in xrange(len_of_target):
                    if source[start + end] != target[end]:
                        break
                if end == len_of_target - 1:
                    return start
        return -1

if __name__ == '__main__':
    assert Solution().strStr("abcde", "e") == 4
