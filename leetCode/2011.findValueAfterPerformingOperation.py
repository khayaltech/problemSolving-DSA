class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
             return sum(1 if '+' in y else -1 for y in operations)

        