class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            coins-=costs[i]
            if coins==0:
                return i+1
            elif coins<=0:
                return i
        return len(costs)
        