# Given an array of strings, return all groups of strings that are anagrams.
# sort the words, and store them to the dict based on the sorted word.

class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        mydict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            mydict[sortedword] = [word] if sortedword not in mydict else mydict[sortedword] + [word]
        result = []
        for key, value in mydict.items():
            if len(value) >= 2:
                result += value
        return result
