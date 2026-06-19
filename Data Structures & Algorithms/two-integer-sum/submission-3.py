class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Maps each number to its index: {number: index}
        seen = {}
        
        # Loop through the list tracking both the index and the number
        for i, num in enumerate(nums):
            # Calculate the exact matching number needed to reach the target
            complement = target - num
            
            # If the matching number is already in our dictionary, we found the pair
            if complement in seen:
                # Return the indices with the smaller index first
                return [seen[complement], i]
            
            # Otherwise, save the current number and its index for future checks
            seen[num] = i
