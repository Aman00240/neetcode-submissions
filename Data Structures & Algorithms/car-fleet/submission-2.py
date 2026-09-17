class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[[p,s] for p,s in zip(position,speed)]

        fleet_count=0
        slowest_time_ahead=0.0

        for p,s in sorted(pair)[::-1]:
            time=(target-p)/s

            if time>slowest_time_ahead:
                fleet_count+=1
                slowest_time_ahead=time
        
        return fleet_count