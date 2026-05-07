class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high+1)//2 - low//2)

# Count odd numbers from 0 to high
# minus count odd numbers from 0 to low-1
