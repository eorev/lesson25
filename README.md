# Problem

This program is designed to solve the Traveling Salesman Problem. The goal of this problem is to find the shortest possible route that a traveling salesman can take, given that they must visit each city once and only once, then return to their starting city.

# Solution

The solution is based on a simple greedy algorithm: starting from a given city, the algorithm will choose the nearest unvisited city, mark it as visited, and add it to the route. This process is repeated until all cities have been visited.

The algorithm keeps track of the route taken and the total distance covered. The input to the algorithm is a matrix of distances between cities, which is read from an input file. After running the algorithm on the matrix, the shortest route and the total distance are printed out.