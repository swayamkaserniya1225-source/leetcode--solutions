class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times=times
        self.leaders=[]
        dict1={}
        max_votes=0
        current_leader=-1
        for num in persons:
            dict1[num]=dict1.get(num,0)+1
            if dict1[num]>=max_votes:
                max_votes=dict1[num]
                current_leader=num
            self.leaders.append(current_leader)
    def binary_search(self,x):
        left=0
        right=len(self.times)-1
        while left<=right:
            mid=left+(right-left)//2
            if x==self.times[mid]:
                return mid 
            elif x>self.times[mid]:
                left=mid+1
            else:
                right=mid-1
        return right    
    def q(self, t: int) -> int:
        return self.leaders[self.binary_search(t)]

        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)