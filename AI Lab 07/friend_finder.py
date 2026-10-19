# List of friends in a social network
network = {
    "Ali": ["Bilal", "Sara"],
    "Bilal": ["Ali", "Zara"],
    "Sara": ["Ali", "Omar"],
    "Zara": ["Bilal", "Hira"],
    "Omar": ["Sara"],
    "Hira": ["Zara"],
}

def bfs_shortest_path(graph, start, goal):
    queue = [[start]]
    visited = [start]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(path + [neighbour])

    return None


path = bfs_shortest_path(network, "Ali", "Hira")

if path:
    print("Shortest chain from Ali to Hira:", path)
    print("Number of introductions needed:", len(path) - 1)
else:
    print("No connection found between Ali and Hira.")


network["Hira"].append("Usman")
network["Usman"] = ["Hira"]

print("Updated network:", network)