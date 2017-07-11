class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        if A is None or B is None or len(A) < len(B):
            return False
        if len(B) == 0:
            return True

        mydict = {}
        for a in list(A):
            mydict[a] = mydict.get(a, 0) + 1

        for b in list(B):
            tmp = mydict.get(b, 0) - 1
            if tmp < 0:
                return False
            mydict[b] = tmp
        return True

if __name__ == '__main__':
    assert Solution().compareStrings("ABCD", "ACD") == True
    assert Solution().compareStrings("ABCD", "AABC") == False
    assert Solution().compareStrings("AS", "") == True
