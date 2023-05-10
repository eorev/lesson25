def readInput(fileName):
    try:
        with open(fileName, 'r') as file:
            lines = file.readlines()
            distances = [list(map(int, line.strip().split())) for line in lines]
            return distances
    except FileNotFoundError:
        return f"File {fileName} not found."
    except Exception as e:
        return f"Error when reading file {fileName}: {e}"

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

def main(input_data):
    distances = readInput(input_data)
    path, totalDistance = findShortestPath(distances)
    print('\n'.join(str(vertex) for vertex in path))  # Print the path
    print(totalDistance)  # Print the total distance