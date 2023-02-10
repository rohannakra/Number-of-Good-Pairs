# https://leetcode.com/problems/number-of-good-pairs/

def num_identical_pairs(nums):
    pairs = []

    for i in range(len(nums)):
        current_index = i
        for c in range(len(nums)):
            if c == i:
                continue
            else:
                if nums[i] == nums[c]:
                    if sorted((i, c)) in pairs:
                        continue
                    else:
                        pairs.append(sorted((i, c)))
    
    return len(pairs)

print(num_identical_pairs([1, 2, 3, 1, 1, 3]))
print(num_identical_pairs([1, 1, 1, 1]))
print(num_identical_pairs([1, 2, 3]))

# ----------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = []

        for i in range(len(nums)):
            current_index = i
            for c in range(len(nums)):
                if c == i:
                    continue
                else:
                    if nums[i] == nums[c]:
                        if sorted((i, c)) in pairs:
                            continue
                        else:
                            pairs.append(sorted((i, c)))
    
        return len(pairs)
        