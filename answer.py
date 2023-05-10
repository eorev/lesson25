def readInput(fileName):
    try:
        with open(fileName, 'r') as file:
            lines = file.readlines()
            print(f"Lines in the file: {lines}")  # Print the lines read from the file
            distances = [list(map(int, line.strip().split())) for line in lines]
            print(f"Distances: {distances}")  # Print the parsed distances
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
    distances = readInput(fileName)
    path, totalDistance = findShortestPath(distances)
    for vertex in path:
        print(vertex)
    print(totalDistance)


def main(fileName):
    distances = readInput(fileName)
    path, totalDistance = findShortestPath(distances)
    print(' '.join(str(vertex) for vertex in path))
    print(totalDistance)