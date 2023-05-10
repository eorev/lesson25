def readInput(fileName):
    try:
        with open(fileName, 'r') as file:
            lines = file.readlines()
            distances = [list(map(int, line.strip().split())) for line in lines]
            return distances
    except FileNotFoundError:
        print(f"File {fileName} not found.")
    except Exception as e:
        print(f"Error when reading file {fileName}: {e}")
    return None

def findShortestPath(distances):
    n = len(distances)
    visited = [False] * n
    path = []
    currentVertex = 0
    path.append(currentVertex)
    visited[currentVertex] = True

    totalDistance = 0
    for distance in range(n - 1):
        shortestDistance = float('inf')
        nextVertex = -1
        for vertex in range(n):
            if distances[currentVertex][vertex] != 0 and not visited[vertex] and distances[currentVertex][vertex] < shortestDistance:
                shortestDistance = distances[currentVertex][vertex]
                nextVertex = vertex

        currentVertex = nextVertex
        visited[currentVertex] = True
        path.append(currentVertex)
        totalDistance += shortestDistance

    # Adding distance from last vertex to first vertex
    totalDistance += distances[path[-1]][path[0]]

    return path, totalDistance


def main(fileName):
    try:
        distances = readInput(fileName)
        if distances is not None:  # Make sure we have distances to work with
            path, totalDistance = findShortestPath(distances)
            print(' '.join(str(vertex) for vertex in path))
            print(totalDistance)
        else:  # If distances is None, there was a problem reading the file
            print("Error: No distances provided.")
    except Exception as e:
        print(f"Error in main: {e}")