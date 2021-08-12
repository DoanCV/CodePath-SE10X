"""
# we only have one number being duplicated but it can be duplicated multiple times
# we are guranteed a duplicate 

Cyclic sort:
while we are not at the end of the array

  if the current value is in the wrong position

    if the value at the position of the current value is not the same 
      we swap
    otherwise the two values we are swapping are the same then we found our duplicate

  else
    increment the current position

ex. 
nums = [1,4,4,3,2]

i = 0
nums[i] = 1
nums[ nums[i] - 1 ] = 1
same so increment i
nums = [1,4,4,3,2]

i = 1
nums[i] = 4
nums[ nums[i] - 1 ] = 3
not the same so swap
nums = [1,3,4,4,2]

i = 1
nums[i] = 3
nums[ nums[i] - 1 ] = 4
not the same so swap
nums = [1,4,3,4,2]

i = 1
nums[i] = 4
nums[ nums[i] - 1 ] = 4
they are the same numbers so that is our duplicate
"""

def find_duplicate(nums):
  i = 0
  while i < len(nums):
    
    if nums[i] - 1 != i:

      current = nums[i] - 1
      if nums[i] != nums[current]:
        nums[i], nums[current] = nums[current], nums[i]  # swap
      else:  # we have found the duplicate
        return nums[i]

    else:
      i += 1
  # no need to return anything at this point since we are guranteed a number will be duplicated
  
  
# O(N) time complexity, where N is the length of the given array, since in the worst case we complete everything in one loop with no repeated steps.
# O(1) space complexity since we are not using any extra data structures.
