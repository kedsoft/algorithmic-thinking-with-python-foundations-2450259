def key_with_min_value(dict):
    '''
        min(d, key=d.get) finds the key in the dictionary d that has the minimum value.
        The key=d.get argument tells the min function to compare the values in the 
        dictionary rather than the keys.
    '''
    return min(dict, key=dict.get)


def unvisited_node_with_smallest_value(dict, visited):
    return key_with_min_value({k: v for k,v in dict.items() if k not in visited})


def unvisted_neighbours(current_node, graph, visited):
    return [node for node in graph[current_node] if node not in visited]

START = "B"
graph = {
   "A": {"B": 3, "C": 3},
   "B": {"A": 3, "D": 3.5, "E": 2.8},
   "C": {"A": 3, "E": 2.8, "F": 3.5},
   "D": {"B": 3.5, "E": 3.1, "G": 10},
   "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
   "F": {"G": 2.5, "C": 3.5},
   "G": {"F": 2.5, "E": 7, "D": 10},
}


visited = []
distances = {node: float("inf") for node in graph}
distances[START] = 0

while len(visited) < len(graph):
    current_node = unvisited_node_with_smallest_value(distances, visited)
    for neighbour in unvisted_neighbours(current_node, graph, visited):
        potential_new_distance = distances[current_node] + graph[current_node][neighbour]
        if potential_new_distance < distances[neighbour]:
            distances[neighbour] = potential_new_distance
    visited.append(current_node)
    
print(distances)

