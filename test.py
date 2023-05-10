from answer import findShortestPath, readInput

def testShortestPathFromFile():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        print(f"Lines in the file: {lines}")
        distances = [list(map(int, line.strip().split())) for line in lines]
        print(f"Distances: {distances}")
    path, totalDistance = findShortestPath(distances)
    path, totalDistance = findShortestPath(distances)
    print("Selected path:")
    for vertex in path:
        print(vertex)
    print("Total distance:", totalDistance)
    assert len(path) == 15
    assert totalDistance == 291

if __name__ == "__main__":
    testShortestPathFromFile()
    print("Everything passed")