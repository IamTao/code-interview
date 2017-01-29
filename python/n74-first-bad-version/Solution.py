class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        if n == 0:
            return -1

        start, end = 1, n
        while start + 1 < end:
            mid = (start + end) / 2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid
        return start if SVNRepo.isBadVersion(start) else end
