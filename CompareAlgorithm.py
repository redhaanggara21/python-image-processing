# A Python3 program for 
# Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix 
# representation of the graph

# Library for INT_MAX
import sys

#Prim
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to print 
    # the constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initialize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):

        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):

                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False \
                and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

#Back Tracing
class BackTrace():

   def permute(self, list, s):
        if list == 1:
            return s
        else:
            return [ 
                y + x
                for y in self.permute(1, s)
                for x in self.permute(list - 1, s)
            ]

#Prim
class Prim():

    def maxPackedSets(self, items, sets):
   
        # Initialize the maximum number of sets that can be packed to 0
        maxSets = 0
    
        # Loop through all the sets
        for set in sets:
            # Initialize the number of sets that can be packed to 0
            numSets = 0
    
            # Loop through all the items
            for item in items:
                # Check if the current item is in the current set
                if item in set:
                    # If the item is in the set, increment 
                    # the number of sets that can be packed
                    numSets += 1
    
                    # Remove the item from the set of items, 
                    # so that it is not counted again
                    items = [i for i in items if i != item]
    
            # Update the maximum number of sets that can be packed
            maxSets = max(maxSets, numSets)
    
        return maxSets

def main():

    #Prim
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]
    g.primMST()

    # Back Tracing
    # Example 1
    x = BackTrace()
    print(x.permute(1, ["a","b","c"]))
    print(x.permute(2, ["a","b","c"]))

    #Exaustive Search
    # Set of items
    items = [1, 2, 3, 4, 5, 6]
    
    # List of sets
    sets = [
        [1, 2, 3],
        [4, 5],
        [5, 6],
        [1, 4]
    ]
    
    # Find the maximum number of sets that 
    # can be packed into the given set of items
    y = Prim()
    maxSets = y.maxPackedSets(items, sets)
    
    # Print the result
    print(f"Maximum number of sets that can be packed: {maxSets}")
    


if __name__ == "__main__":
    main()

