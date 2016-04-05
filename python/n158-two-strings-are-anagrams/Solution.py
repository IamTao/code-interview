# -*- coding: utf-8 -*-
#
# An anagram is a type of word play, the result of rearranging the letters of a
# word or phrase to produce a new word or phrase, using all the original letters
# exactly once


class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        return self.anagram1(s, t)
        return self.anagram2(s, t)

    def anagram2(self, s, t):
        if len(s) != len(t):
            return False
        s = sorted(list(s))
        t = sorted(list(t))

        for ind in xrange(len(s)):
            if s[ind] != t[ind]:
                return False
        return True

    def anagram1(self, s, t):
        # write your code here
        if len(s) != len(t):
            return False

        mydict = {}
        for le in s:
            mydict[le] = mydict.get(le, 0) + 1

        for le in t:
            if le in mydict and mydict[le] >= 0:
                mydict[le] = mydict[le] - 1
            else:
                return False
        if len(filter(lambda x: x < 0, mydict.values())) > 0:
            return False
        return True

if __name__ == '__main__':
    assert Solution().anagram("django", "naogdj")
