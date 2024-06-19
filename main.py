# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        count = set()
        for index in nums:
            if index in count:
                return True
            else:
                count.add(index)


# Time Complexity: O(n)
# Since the "if" check and the "add" operation are both O(1) and they are performed once for each of the 𝑛 elements, the total time complexity is O(1).


# Space Complexity: O(n)
# Storage for the set (count):

# In the worst case, if all elements in the list are unique, the set will store all 𝑛 elements. Therefore, the space complexity for the set is O(n)
# Additional variables:
# The only other variable used is "index", which takes O(1) space.
# Combining these, the overall space complexity is dominated by the space needed to store the elements in the set, which is: O(n)
