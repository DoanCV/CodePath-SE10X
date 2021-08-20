"""
BFS since we want all distinct subsets
input: [1, 5, 3]
output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

                          []
                /         |         \
              [1]        [5]        [3]
             /   \      /   \       /  \
           [5]   [3]  [1]   [3]   [1]  [5]
                          .
                          .
                          .
nah this doesnt get uniques

try this
  go through the array once from left to right
  start with an empty set
    for each element in the array add it to all of the existing subsets
  
  ex. [1, 5, 3]
  []                          # we have empty list
  [ [] ]                      # empty set
  [ [] , [1] ]                # for each element in the array add it to all of the existing subsets, which is just the empty set
  [ [] , [1], [3], [1,3] ]    # repeat, in this case we have empty set and a set with just the first element, add the second element to each as a new unique set
  [ [] , [1], [3], [1,3], [5], [1,5], [3,5], [1,3,5] ]    # repeat

sticking to trees it looks like

                     []
                    /  \
                  []    [1]
                    /  \
              [],[1]    [3],[1,3]
                    /  \
      [],[1],[3],[1,3]  [5],[1,5],[3,5],[1,3,5]

left is copy and right is new addition to the left
"""

def find_subsets(nums):
  subsets = []
  
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
