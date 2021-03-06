"""
Itinerary has to use all of the edges, i.e. tickets, once
    this is euler circuit
    
we are guranteed that all itineraries start with JFK and that there is a valid itinerary



create an adjacency list
    hashmap = {vertex: [connected veritices, we will sort this to get the correct lexical order]}

we will DFS starting from "JFK"
    get the first destination from the sorted list given a from_vertex
    then recurse on that destination
    
    add the from_vertex to the itinerary
    
the itinerary we build is backwards since we append to a path when we see no other destinations left


ex
a -> b -> c -> d
    | ^-----
    -> e ->|
    
we start at a and get rid of edge a,b
    then say we go into c since it is lexical so we get rid of edge b,c
    then c,d
    there is nothing leaving d so we add that first to our itinerary
        we go back up to c, add that
    then at b we go to e and get rid of b,e then e,b
        there is nothing leaving b so we add b
        we go back up to e, add that
        back to b, add that
    back up to a, add that
result = [d,c,b,e,b,a]
reversed result, i.e. correct answer = [a,b,e,b,c,d]

O(E * logE) where E is the number of edges since we sort each list in the adjacency list.
"""
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        self.adjacency_list = defaultdict()
        for u, v in tickets:
            self.adjacency_list[u].append(v)
        
        for u in self.adjacency_list:
            self.adjacency_list[u].sort()
        
        self.itinerary = []
        self.dfs("JFK")
        return self.itinerary[::-1]
    
    def dfs(self, from_vertex):
        while self.itinerary.[from_vertex]:
            to_vertex = self.itinerary.[from_vertex].pop(0)
            self.dfs(to_vertex)
        
        self.itinerary.append(from_vertex)
