class Solution(object):
    def longestSubsequence(self, s, k):
        power = 0
        count = 0
        val = 0
        n = len(s)

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                count += 1
            else:
                if power < 32:
                    val += (1 << power)
                    if val <= k:
                        count += 1
            power += 1
        return count