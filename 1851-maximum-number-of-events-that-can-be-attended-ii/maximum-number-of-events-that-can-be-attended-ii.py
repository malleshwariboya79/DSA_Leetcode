from bisect import bisect_right

class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort(key=lambda x: x[0])
        starts = [e[0] for e in events]
        n = len(events)
        nxt = [0] * n
        for i, (_, end, _) in enumerate(events):
            nxt[i] = bisect_right(starts, end)
        dpPrev = [0] * (n + 1)
        dpCurr = [0] * (n + 1)
        for _ in range(1, k+1):
            for i in range(n-1, -1, -1):
                dpCurr[i] = max(dpCurr[i+1], events[i][2] + dpPrev[nxt[i]])
            dpPrev, dpCurr = dpCurr, dpPrev
        return dpPrev[0]