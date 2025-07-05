class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d=Counter(arr)
        m=0
        for i,j in d.items():
            if i ==j:
                m=max(m,i)
        return m if m!=0 else -1