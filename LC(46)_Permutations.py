from itertools import permutations, combinations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))