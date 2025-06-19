class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        count = 0
        n = len(strs)
        m = len(strs[0])

        for c in range(m):
            for r in range(1, n):
                if strs[r][c] < strs[r - 1][c]:
                    count += 1
                    break  

        return count
