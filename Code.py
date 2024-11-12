from bisect import bisect_right
from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Step 1: Sort items by price
        items.sort(key=lambda x: x[0])
        
        # Step 2: Preprocess the max beauty for each price threshold
        max_beauty = []
        current_max = 0
        
        for price, beauty in items:
            current_max = max(current_max, beauty)
            max_beauty.append((price, current_max))  # Store price and the max beauty at that price
        
        # Step 3: Answer the queries using binary search
        result = []
        
        for query in queries:
            # Binary search to find the right-most item with price <= query
            idx = bisect_right(max_beauty, (query, float('inf'))) - 1
            if idx == -1:
                result.append(0)  # No item with price <= query
            else:
                result.append(max_beauty[idx][1])  # Return the max beauty for that price
        
        return result
