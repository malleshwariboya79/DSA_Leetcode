import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda a:(a[0], a[1]))

        last = max(event[1] for event in events)
        n = len(events)
        pq = []
        j = 0 # pointer for events
        ans = 0
        for i in range(1, last + 1):
            # put all available events in pq
            while j < n and events[j][0] <= i:
                heapq.heappush(pq, events[j][1])
                # print(f"event [{i}, {j}] has been added")
                j += 1
            # pop all events that ended
            while pq and pq[0] < i:
                # print(f"event has ended on {pq[0]}")
                heapq.heappop(pq)

            
            # attend shortest event
            if pq:
                # print(f"on day {i}, attending event that ends on {pq[0]}")
                ans += 1
                heapq.heappop(pq)
        return ans
        