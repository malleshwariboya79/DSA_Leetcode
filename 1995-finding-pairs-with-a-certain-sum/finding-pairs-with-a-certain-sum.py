class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.dic=defaultdict(int)
        for i in nums1:
            self.dic[i]+=1
        self.arr=[k for k in nums2]
        self.dic2=defaultdict(int)
        for i in nums2:
            self.dic2[i]+=1

    def add(self, index: int, val: int) -> None:
        old=self.arr[index]
        self.arr[index]+=val
        self.dic2[old]-=1
        self.dic2[old+val]+=1

    def count(self, tot: int) -> int:
        ans=0
        for i in self.dic:
            ans+=self.dic2[tot-i]*(self.dic[i])
        return ans