class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = 0
        sum_cost = 0

        for i in range(len(gas)):
            sum_gas += gas[i]
            sum_cost += cost[i]
        
        if sum_gas < sum_cost:
            return -1 

        total_tank = 0
        start_station = 0

        for i in range(len(gas)-1):
            total_tank += gas[i]-cost[i]

            if total_tank < 0:
                start_station = i+1
                total_tank = 0

        return start_station 