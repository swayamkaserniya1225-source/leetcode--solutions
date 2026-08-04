class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        current_sum=0
        pos=0
        for i in range(len(gas)):
            current_sum+=(gas[i]-cost[i])
            if current_sum<0:
                pos=i+1
                current_sum=0
        return pos


