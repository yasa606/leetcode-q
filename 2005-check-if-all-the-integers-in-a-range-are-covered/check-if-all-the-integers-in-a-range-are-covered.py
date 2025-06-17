class Solution:
    def isCovered(self, ranges, left, right):
       
        covered = [False] * 51

        for s, e in ranges:
            for i in range(s, e + 1):
                covered[i] = True

        for i in range(left, right + 1):
            if not covered[i]:
                return False

        return True
