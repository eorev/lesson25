def readInput(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            distances = [list(map(int, line.strip().split())) for line in lines]
            return distances
    except FileNotFoundError:
        return f"File {filename} not found."
    except Exception as e:
        return f"Error when reading file {filename}: {e}"

def findShortestPath(distances):
    n = len(distances)
    visited = [False] * n
    path = []
    currentVertex = 0
    path.append(currentVertex)
    visited[currentVertex] = True

    totalDistance = 0
    for _ in range(n - 1):
        shortestDistance = float('inf')
        nextVertex = -1
        for vertex in range(n):
            if not visited[vertex] and distances[currentVertex][vertex] < shortestDistance:
                shortestDistance = distances[currentVertex][vertex]
                nextVertex = vertex

        if nextVertex == -1:  # If there are no more reachable vertices, find the closest unvisited vertex
            for vertex in range(n):
                for otherVertex in range(n):
                    if not visited[vertex] and distances[currentVertex][otherVertex] < shortestDistance:
                        shortestDistance = distances[currentVertex][otherVertex]
                        nextVertex = vertex

        currentVertex = nextVertex
        visited[currentVertex] = True
        path.append(currentVertex)
        totalDistance += shortestDistance

    # Adding distance from last vertex to first vertex
    totalDistance += distances[path[-1]][path[0]]

    return path, totalDistance

def main(filename):
    distances = readInput(filename)
    path, totalDistance = findShortestPath(distances)
    print('\n'.join(str(vertex) for vertex in path))  # Print the path
    print(totalDistance)  # Print the total distance

if __name__ == "__main__":
    main("input.txt")