# https://leetcode.com/problems/destination-city/

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        final_destinations = set()
        not_final_destinations = set()
        for city1, city2 in paths:
            not_final_destinations.add(city1)

            if city1 in final_destinations:
                final_destinations.remove(city1)

            if city2 in not_final_destinations:
                if city2 in final_destinations:
                    final_destinations.remove(city2)
            else:
                final_destinations.add(city2)

        return final_destinations.pop()


