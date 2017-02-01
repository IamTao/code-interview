class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if sum(gas) < sum(cost):
            return -1
        num_station = len(gas)
        left = 0
        start_station = 0
        for i in range(num_station):
            if gas[i] + left < cost[i]:
                start_station = i + 1
                left = 0
            else:
                left += gas[i] - cost[i]
        return start_station
