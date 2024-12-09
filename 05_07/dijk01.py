inf = float("infinity")

# Define graph as dictionary representing adjacency list.
graph = {
    "U": {"V": 6, "W": 7},
    "V": {"U": 6, "X": 10},
    "W": {"U": 7, "X": 1},
    "X": {"W": 1, "V": 10}
}

visited = []
unvisited = list(graph)

distances = {item: inf for item in graph}


for node in graph:
    for neighbour in graph[node]:
        print(neighbour, end=" | ")
    print()