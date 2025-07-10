class Solution:
    def maxFreeTime(self, event: int, start: List[int], end: List[int]) -> int:
        start+=[event]
        end=[0]+end
        n=len(start)
        maxGap=0

        # create gaps
        gaps=[0]*n      
        for i in range(n):
            gaps[i]=start[i]-end[i]        

        # left and right max array
        leftMax=gaps[:]
        for i in range(1,n):
            leftMax[i]=max(leftMax[i],leftMax[i-1])
        
        rightMax=gaps[:]
        for i in range(n-2,-1,-1):
            rightMax[i]=max(rightMax[i],rightMax[i+1])

        # sliding window
        for i in range(1,n):
            # if event can fill other gaps
            if (i-2>=0 and end[i]-start[i-1]<=leftMax[i-2]) or (i+1<=n-1 and end[i]-start[i-1]<=rightMax[i+1]):
                maxGap=max(maxGap,gaps[i]+gaps[i-1]+end[i]-start[i-1])     
            else:
                maxGap=max(maxGap,gaps[i]+gaps[i-1])
        
        return maxGap