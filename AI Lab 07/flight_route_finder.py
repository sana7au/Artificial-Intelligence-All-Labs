# Dictionary representing the flight routes and their ticket prices
flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": [],
}

def path_cost(path):
    return sum(cost for _, cost in path)

def ucs_cheapest_route(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    explored_paths = []

    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]

        route = [city for city, cost in path]
        cost = path_cost(path)
        explored_paths.append(route)

        print("Exploring path:", route, "| Cost:", cost)

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            return route, cost, len(explored_paths)

        for neighbour, ticket_price in graph.get(node, []):
            queue.append(path + [(neighbour, ticket_price)])

    return None, None, len(explored_paths)


route, total_cost, explored_count = ucs_cheapest_route(
    flights, "Islamabad", "Quetta"
)

if route:
    print("Cheapest route:", route)
    print("Total ticket cost:", total_cost)
else:
    print("No route found.")